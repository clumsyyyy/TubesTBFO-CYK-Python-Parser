from CNF import CNF_Equals
from CYKcheck import CYKCHECKCLASS
from LOOP_FA_function import FA_function_HELPER
from FA_varchecker import FA_VALIDFUNVARNAMEC
from BOOL_parser import FA_boolean
class FA_equals:
    def checkEqual(self, str):
        strArr = [x for x in ' '.join(str.strip().split())]
        equalArr =  ['+=', '-=', '//=', '*=', '/=', '%=', "**=", "=", ":=", "@="]
        singletonIdents = ["+", "-", "/", "*", "%", "=", ":", "@"]
        equalCount = 0
        equalSign = ""
        token = ""
        word = []

        for i in range(len(strArr)):
            if strArr[i] not in singletonIdents:
                token += strArr[i]
            else:
                equalSign += strArr[i]
                if strArr[i] == "=":
                    word.append(equalSign)
                    break

        word = [token.strip(), equalSign, ''.join(strArr[i + 1:]).strip() ]

        if equalSign == "":
            raise Exception(["No equal sign"])
        elif equalCount > 1:
            raise Exception(["Too many equal signs"])

        
        #cek sisi kiri harusnya variabel
        varCheck = FA_VALIDFUNVARNAMEC()
        try:
            varCheck.check(word[0])
        except Exception as e:
            raise e
        else:
            word[0] = "VAR"     
 

        #cek sisi kanan

        funcCheck = FA_function_HELPER()
        boolCheck = FA_boolean()
        print(word)
        try:
            funcCheck.checkList(word[2])
        except Exception as e:
            try:
                funcCheck.checkArith(word[2])
            except Exception as e:
                try:
                    varCheck.check(word[2])
                except Exception as e:
                    try:
                        funcCheck.checkfuncall(word[2])
                    except Exception as e:
                        try:
                            boolCheck.checkBoolStatement(word[2])
                        except Exception as e:
                            if ("\"" in word[2] and word[2].count("\"") % 2 == 0) or word[2].isdigit() and not funcCheck.checkList(word[2]):
                                word[2] = "ASSIGN"
                            else:
                                word[2] = "INVALID"
                        else:
                            word[2] = "BOOL"
                    else:
                        word[2] = "FUNCALL"
                else:
                    word[2] = "VAR"
            else:
                word[2] = "ARITH"
        else:
            word[2] = "LIST"

        CYKChecker = CYKCHECKCLASS()
        print(word)
        CNF = CNF_Equals()
        if CYKChecker.check(CNF.getNewEqRule(), word):
            return True
        else:
            raise Exception(["Grammar incompatible!"])