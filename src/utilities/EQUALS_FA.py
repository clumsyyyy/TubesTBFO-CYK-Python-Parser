from ARITH_helper import arithHelper
#from LIST_helper import listHelper
from CNF_general import CNF_Equals
from CYKCHECKER_general import CYKCHECKCLASS
from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER

class FA_equals:
    def checkEqual(self, str):
        strArr = str.split()
        equalArr = ['=', '+=', '-=', '//=', '*=', '/=', '%=', "**="]
        equalCount = 0
        equalSign = ""
        for i in range(len(strArr)):
            for j in range(len(equalArr)):
                if strArr[i] == equalArr[j]:
                    equalSign = equalArr[j]
                    equalCount += 1;
        if equalCount == 0:
            raise Exception(["No equal sign"])
        elif equalCount > 1:
            raise Exception(["Too many equal signs"])
        word = str.split(equalSign)
        word.insert(1, equalSign)
        
        #cek sisi kiri harusnya variabel
        varCheck = FA_VALIDFUNVARNAMEC()
        for i in range(len(word)):
            word[i] = word[i].replace(" ", "")
        
        print(word)
        try:
            varCheck.check(word[0])
        except Exception as e:
            raise e
        else:
            word[0] = "VAR"     
 

        #cek sisi kanan
        arithCheck = arithHelper()
        funcCheck = FA_function_HELPER()
        #listCheck = listHelper()
        print(word)
        # try:
        #     listCheck.checkList(word[2])
        # except Exception as e:
        try:
            arithCheck.checkArithStatement(word[2])
        except Exception as e:
            try:
                varCheck.check(word[2])
            except Exception as e:
                try:
                    funcCheck.checkfuncall(word[2])
                except Exception as e:
                    if ("\"" in word[2] and word[2].count("\"") % 2 == 0) or word[2].isdigit() and not listCheck.checkList(word[2]):
                        word[2] = "ASSIGN"
                    else:
                        word[2] = "INVALID"
                else:
                    word[2] = "FUNCALL"
            else:
                word[2] = "VAR"
        else:
            word[2] = "ARITH"
        # else:
        #     word[2] = "LIST"

        CYKChecker = CYKCHECKCLASS()
        print(word)
        CNF = CNF_Equals()
        if CYKChecker.check(CNF.getEqualsRule(), word):
            return True
        else:
            raise Exception(["Grammar incompatible!"])