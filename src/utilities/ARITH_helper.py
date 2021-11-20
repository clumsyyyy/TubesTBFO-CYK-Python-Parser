from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER

class arithHelper:
    def checkArithStatement(self, string):
        arithOps = ["+", "-", "/", "//", "%", "*"]
        arithFlag = False
        for i in range(len(arithOps)):
            if arithOps[i] in string:
                arithFlag = True
        for i in range(len(arithOps)):
            if (string[0] == arithOps[i] or string[-1] == arithOps[i]) and arithOps[i] != "-":
                raise Exception("misplaced operator")

        if arithFlag == False:
            raise Exception("No operator in sentence")
        
        openingBracketCount = string.count("(")
        closingBracketCount = string.count(")")
        if (openingBracketCount != closingBracketCount):
            raise Exception("Non-matching brackets")
        arithCount = 0
        for i in range(len(arithOps)):
            if arithOps[i] in string:
                if (arithOps[i] == "-"):
                    arr = [x for x in string]
                    for j in range(len(arr)):
                        if arr[j] == "-" and not arr[j + 1].isdigit():
                            arithCount += 1
                elif (arithOps[i] == "/"):
                    arr = [x for x in string]
                    for j in range(len(arr)):
                        if arr[j] == "/" and (arr[j + 1] != "/" and arr[j - 1] != "/"):
                            arithCount += 1
                else:
                    arithCount += string.count(arithOps[i])

        if "(" in string:
            string = string.replace("(", "")
        if ")" in string:
            string = string.replace(")", "")
        if (arithCount >= len(self.arithTokenizer(string))):
            raise Exception("Too many arithmetic operators")
        else:
            return True
    
    def arithTokenizer(self, string):
        num_arr = []
        arr = [x for x in string]
        arithOps = ["+", "-", "/", "//", "%", "*"]
        count = ""
        minusFlag = False
        for i in range(len(arr)):
            if arr[i].isdigit() or arr[i].isalpha():
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
                    if count.isdigit():
                        if minusFlag:
                            minusFlag = False
                            num_arr.append(int(count) * -1)
                        else:
                            num_arr.append(int(count))
                        count = ""
                    else:
                        num_arr.append(count)
        if count != "":
            if count.isdigit():
                if minusFlag:
                    minusFlag = False
                    num_arr.append(int(count) * -1)
                else:
                    num_arr.append(int(count))
                count = ""
            else:
                num_arr.append(count)
        print(num_arr)

        varCheck = FA_VALIDFUNVARNAMEC()
        for i in range(len(num_arr)):
            if not str(num_arr[i]).lstrip("-").isdigit():
                try:
                    varCheck.check(num_arr[i])
                except Exception as e:
                    raise e
   
        return num_arr