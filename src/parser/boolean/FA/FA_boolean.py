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


    def checkComparisonStatement(self, str):
        comparisonOps = ["<", "<=", ">", ">=", "==", "!="]
        opsCount = 0;
        for i in range(len(comparisonOps)):
            if (comparisonOps[i] in str):
                opsCount += 1
                word = str.split(comparisonOps[i])
        if (opsCount > 1):
            raise Exception("More than one comparison operator detected")

        #cek arithmetic
        instArith = arithHelper()
        for i in range(len(word)):
            instArith.checkArithStatement(word[i].replace(" ", ""))
class arithHelper:
    def checkArithStatement(self, str):
        arithOps = ["+", "-", "/", "//", "%", "*"]
        openingBracketCount = str.count("(")
        closingBracketCount = str.count(")")
        if (openingBracketCount != closingBracketCount):
            raise Exception("Non-matching brackets")
        arithCount = 0
        for i in range(len(arithOps)):
            if arithOps[i] in str:
                if (arithOps[i] == "-"):
                    arr = [x for x in str]
                    for j in range(len(arr)):
                        if arr[j] == "-" and not arr[j + 1].isdigit():
                            arithCount += 1
                elif (arithOps[i] == "/"):
                    arr = [x for x in str]
                    for j in range(len(arr)):
                        if arr[j] == "/" and (arr[j + 1] != "/" and arr[j - 1] != "/"):
                            arithCount += 1
                else:
                    arithCount += str.count(arithOps[i])

        if "(" in str:
            str = str.replace("(", "")
        if ")" in str:
            str = str.replace(")", "")
        
        if (arithCount >= len(self.arithTokenizer(str))):
            raise Exception("Too many arithmetic operators")
    
    def arithTokenizer(self, str):
        num_arr = []
        arr = [x for x in str]
        count = ""
        minusFlag = False
        for i in range(len(arr)):
            if arr[i].isdigit():
                count += arr[i]
            elif arr[i] == "-":
                if arr[i + 1].isdigit() and arr[i - 1] != "-":
                    minusFlag = True
                elif (arr[i + 1] == "-"):
                    if count != "":
                        if minusFlag:
                            minusFlag = False
                            num_arr.append(int(count) * -1)
                        else:
                            num_arr.append(int(count))
                        count = ""
            else:
                if count != "":
                    if minusFlag:
                        minusFlag = False
                        num_arr.append(int(count) * -1)
                    else:
                        num_arr.append(int(count))
                    count = ""
            if count != "":
                    if minusFlag:
                        minusFlag = False
                        num_arr.append(int(count) * -1)
                    else:
                        num_arr.append(int(count))
                    count = ""
        print(num_arr)
        return num_arr