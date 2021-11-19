# from loop.FA import FA_function
# funcChecker = FA_function.FA_function_HELPER()
import sys
import os
srcfold = "C:\\Users\\OWEN\\OneDrive\\Documents\\IF Sem 3\\TBFO\\Tubes\\TubesTBFO\\src\\"
cykpath = "cykcheck\\"
cnfpath = "parser\\boolean\\"
sys.path.append(os.path.abspath(srcfold + cykpath))
sys.path.append(os.path.abspath(srcfold + cnfpath))

class FA_boolean:
    #the exceptions are still ambiguous because im confused
    #ini buat and/not/or
    def checkBoolStatement(self, str):
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
        
        
        if (len(word) > 5):
            raise Exception("Too many arguments")

        if ("and" not in word and "or" not in word):
            raise Exception("No keyword 'and/or' in statement")

        if (word[0] == "not"):
            if (word[2] != "and" and word[2] != "or"):
                raise Exception("'And/or' keyword misplaced")

        '''
        UNCOMMENT KALO CUMAN TRUE/FALSE
        elif (word[i + 1] != "True" and word[i + 1] != "False"):
            raise Exception("not harusnya diikutin True/False")
        '''
        
        # elif (not funcChecker.checkfuncall(word[i + 1], True)):
            # raise Exception("ada nama fungsi yang tidak valid")
        openingBracketCount = 0
        closingBracketCount = 0
        # asumsi kasusnya masih nerima True/False dulu
        for i in range(len(word)):
            if ("not" in word[i]):
                if ("True" in word[i] or "False" in word[i]):
                    raise Exception("'not' should be separated")
                elif word[i + 1] == "and" or word[i + 1] == "or":
                    if (len(word[i]) == 3):
                        raise Exception("'not' should be followed by a constant/variable")
                    else:
                        arr = [x for x in word[i]]
                        varFlag = False
                        j = 0
                        while (not varFlag and j < len(arr)):
                            print(arr[j])
                            if (arr[j].isnumeric()):
                                varFlag = True
                            j += 1
                        if varFlag == False:
                            raise Exception("'not' should be followed by a constant/variable")
            if ("(" in word[i][0]):
                if ("and" in word[i] or "or" in word[i]):
                    raise Exception("'and/or' operator should not have an opening bracket")
                else:
                    openingBracketCount += word[i].count("(")
            if (")" in word[i][-1]):
                if ("and" in word[i] or "or" in word[i] or "not" in word[i]):
                    raise Exception("'and/or/not' operator should not have a closing bracket")
                else:
                    closingBracketCount += word[i].count(")")

        if openingBracketCount != closingBracketCount:
            raise Exception("open bracket detected but no close bracket")
        
    '''
    def checkComparisonStatement(self, str):
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
        
        comparisonOps = ["<", "<=", ">", ">=", "=="]
        if (word[1] not in comparisonOps):
            raise Exception("Comparison operator invalid")
    '''
        
