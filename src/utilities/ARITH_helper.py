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
        return num_arr