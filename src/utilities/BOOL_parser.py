from CNF import CNF_Boolean
from CYKcheck import CYKCHECKCLASS
from LOOP_FA_function import FA_function_HELPER
from FA_varchecker import FA_VALIDFUNVARNAMEC
class FA_boolean:
    #the exceptions are still ambiguous because im confused
    #ini buat and/not/or
    def checkBoolStatement(self, str):
        funVarCheck = FA_VALIDFUNVARNAMEC()
        funcNameCheck = FA_function_HELPER() 
        word = []
        buffer = ""
        length = len(str)
        for i in range(0, length):
            if (str[i] == " "):
                word.append(buffer)
                buffer = ""
            else:
                buffer += str[i]
        if (buffer != ""):
            word.append(buffer)
        word = list(filter(lambda a: a != "", word))
        
        openingBracketCount = 0
        closingBracketCount = 0
        # asumsi kasusnya masih nerima True/False dulu
        for i in range(len(word)):            
            if ("(" in word[i]):
                if ("and" in word[i] or "or" in word[i]):
                    raise Exception(["'and/or' operator should not have an opening bracket"])
                else:
                    openingBracketCount += word[i].count("(")
            if (")" in word[i]):
                if ("and" in word[i] or "or" in word[i] or "not" in word[i]):
                    raise Exception(["'and/or/not' operator should not have a closing bracket"])
                else:
                    closingBracketCount += word[i].count(")")
        
        
        for i in range(len(word)):
            if word[i][0] == "(": word[i] = word[i][1:]
            if word[i][-1] == ")" and word[i][-2] != "(": word[i] = word[i][:-1]
        arr = ["not", "and", "or", "True", "False", "is"]
        tokenWord = []
        token = ""
        for i in range(len(word)):
            if word[i] in arr:
                if word[i] == "not":
                    tokenWord.append(word[i])
                    if token != "":
                        tokenWord.append(token)
                        token = ""
                elif word[i] == "and" or word[i] == "or":
                    if token != "":
                        tokenWord.append(token)
                        token = ""
                    tokenWord.append(word[i])
                else:
                    token += word[i]
            else:
                token += word[i]
        if token != "":
            tokenWord.append(token)
        word = tokenWord
        print(word)
        for i in range(len(word)):
            if word[i] not in arr:
                if word[i].isdigit():
                    word[i] = "INT"
                else:
                    try:
                        funcNameCheck.checkFunction(word[i])
                    except Exception as e:
                        try:
                            funVarCheck.check(word[i])
                        except Exception as e:
                            try:
                                self.checkComparisonStatement(word[i])
                            except Exception as e:
                                word[i] = "INVALID"
                                raise e  
                            else:
                                word[i] = "COMPARISON"
                        else:
                            word[i] = "VAR"
                    else:
                        word[i] = "FUNCALL"

        if openingBracketCount != closingBracketCount:
            raise Exception(["Mismatching bracket count"])
        for i in range(len(word)):
            if "(" in word[i]:
                word[i] = word[i].replace("(", "")
            if ")" in word[i]:
                word[i] = word[i].replace(")", "")

        CYKChecker = CYKCHECKCLASS()
        CNF = CNF_Boolean()
        boolRule = CNF.getBoolRule()
        if "is" in word:
            boolRule = CNF.getIsRule()
        if CYKChecker.check(boolRule, word):
            return True
        else:
            raise Exception(["Grammar incompatible!"])

    def checkComparisonStatement(self, str):
        comparisonOps = [ "<=", ">=", ">", "<", "==", "!="]
        opsCount = 0;
        for i in range(len(comparisonOps)):
            if (comparisonOps[i] in str):
                opsCount += 1
                word = str.split(comparisonOps[i])
                break
        if (opsCount == 0):
            raise Exception(["No comparison operator"])
        if (opsCount > 1):
            raise Exception(["More than one comparison operator detected"])
        #cek arithmetic
        instArith = FA_function_HELPER()
        var = FA_VALIDFUNVARNAMEC()
        for i in range(len(word)):
            if not word[i].replace(" ", "").isdigit():
                try:
                    instArith.checkArith(word[i].replace(" ", ""))
                except Exception as e:
                    try:
                        var.check(word[i].replace(" ", ""))
                    except Exception as e:
                        raise e
