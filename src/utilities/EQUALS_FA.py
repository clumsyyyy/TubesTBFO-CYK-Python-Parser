from ARITH_helper import arithHelper
from LIST_helper import listHelper
from CNF_general import CNF_Equals
from CYKCHECKER_general import CYKCHECKCLASS
from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER
import re

class FA_equals:
    def checkEqual(self, str):
        if "=" not in str:
            raise Exception("where =")

        word = str.split("=")
        word.insert(1, '=')
        
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
        listCheck = listHelper()
        try:
            listCheck.checkList(word[2])
        except Exception as e:
            try:
                arithCheck.checkArithStatement(word[2])
            except Exception as e:
                try:
                    varCheck.check(word[2])
                except Exception as e:
                    try:
                        funcCheck.checkfuncall(word[2])
                    except Exception as e:
                        print(listCheck.checkList(word[2]))
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
        else:
            word[2] = "LIST"

        CYKChecker = CYKCHECKCLASS()
        print(word)
        CNF = CNF_Equals()
        if CYKChecker.check(CNF.getEqualsRule(), word):
            return True
        else:
            raise Exception("Grammar incompatible!")