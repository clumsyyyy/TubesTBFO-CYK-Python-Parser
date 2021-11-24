from CNF import CNF_Equals
from CYKcheck import CYKCHECKCLASS
from LOOP_FA_function import FA_function_HELPER
from FA_varchecker import varNameChecker
class equalsParser:
    def checkEqual(self, str):
        strArr = [x for x in ' '.join(str.strip().split())]
        equalArr =  ['+=', '-=', '//=', '*=', '/=', '%=', "**=", "=", ":=", "@="]
        singletonIdents = ["+", "-", "/", "*", "%", "=", ":", "@"]
        equalCount = 0
        equalSign = ""
        token = ""
        word = []
        bracketFlag = 0
        for i in range(len(strArr)):
            if strArr[i] not in singletonIdents:
                token += strArr[i]
                if strArr[i] == "[":
                    bracketFlag = True
                elif strArr[i] == "]":
                    bracketFlag = False
            else:
                if bracketFlag:
                    #print(strArr[i])
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
        varCheck = varNameChecker()
        funcCheck = FA_function_HELPER()
        boolCheck = FA_function_HELPER()
        try:
            varCheck.check(word[0])
        except Exception as e:
            try:
                funcCheck.checkListElCall(word[0])
            except Exception as e:
                word[0] = "INVALID"
            else:
                word[0] = "LISTEL"
        else:
            word[0] = "VAR"     
 
        #cek sisi kanan
        try:
            funcCheck.checkString(word[2])
        except Exception as e:
            try:
                funcCheck.checkInt(word[2])
            except Exception as e:
                try:
                    funcCheck.checkList(word[2])
                except Exception as e:
                    try:
                        varCheck.check(word[2])
                    except Exception as e:
                        try:
                            funcCheck.checkFunction(word[2])
                        except Exception as e:
                            try:
                                funcCheck.checkArith(word[2])
                            except Exception as e:
                                try:
                                    funcCheck.checkBool(word[2])
                                except Exception as e:
                                    if ("\"" in word[2] and word[2].count("\"") % 2 == 0) or word[2].isdigit() and not funcCheck.checkList(word[2]):
                                        word[2] = "ASSIGN"
                                    else:
                                        word[2] = "INVALID"
                                else:
                                    word[2] = "BOOL"
                            else:
                                word[2] = "ARITH"
                        else:
                            word[2] = "FUNCALL"
                    else:
                        word[2] = "VAR"
                else:
                    word[2] = "LIST"
            else:
                word[2] = "INT"
        else:
            word[2] = "ASSIGN"

        CYKChecker = CYKCHECKCLASS()
        CNFEq = CNF_Equals()
        if CYKChecker.check(CNFEq.getEqualsRule(), word):
            return True
        else:
            raise Exception(["Grammar incompatible!"])
            

