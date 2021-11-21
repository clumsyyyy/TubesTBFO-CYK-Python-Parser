from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER

class arithHelper:
    def checkArithStatement(self, string):
        instValid = FA_VALIDFUNVARNAMEC()
        if (string.isdigit()):
            return True
        arithOps = ["+", "-", "/", "//", "%", "*", "**"]
        opsSingleton = ["+", "-", "*", "/", "%"]
        openingBracketCount = string.count("(")
        closingBracketCount = string.count(")")
        if (openingBracketCount != closingBracketCount):
            raise Exception(["Non-matching brackets"])
        arithFlag = False
        for i in range(len(arithOps)):
            if arithOps[i] in string:
                arithFlag = True
                break
        if arithFlag == False:
            raise Exception(["No operator in sentence"])
        wordSep = []
        operand = ""
        for i in string:
            if i in ["(", ")"]:
                if operand != "":
                    wordSep.append(operand)
                    operand = ""
                wordSep.append(i)
            else:
                operand = operand + i
        if operand != "":
            wordSep.append(operand)
        openInsideFirstBracket = 0
        f = True
        wslen = len(wordSep)
        parsedWord = []
        insideapp = ""
        isThereParen = False
        for i in range(wslen):
            if wordSep[i] == "(":
                isThereParen = True
                if f:
                    parsedWord.append("(")
                    f = False
                else:
                    openInsideFirstBracket += 1
                    insideapp += wordSep[i]
            elif wordSep[i] == ")":
                if openInsideFirstBracket == 0:
                    parsedWord.append(insideapp)
                    parsedWord.append(wordSep[i])
                    insideapp = ""
                    f = True
                else:
                    openInsideFirstBracket -= 1
                    insideapp += wordSep[i]
            else:
                if (f == True):
                    parsedWord.append(wordSep[i])
                else:
                    insideapp += wordSep[i]
        
        #parsedWord = [x.strip() for x in parsedWord]
        pwlen = len(parsedWord)
        if isThereParen:
            exprFlag = False
            for i in range(pwlen):
                if parsedWord[i] == "(":
                    exprFlag = True
                elif parsedWord[i] == ")":
                    exprFlag = False
                else:
                    if exprFlag == True:
                        if (self.checkArithStatement(parsedWord[i])):
                            parsedWord[i] = "VALID"
                        else:
                            raise Exception(["Invalid expression"])
        parsedStr = "".join(parsedWord)
        toappend = ""
        word = []
        for i in parsedStr:
            if i in opsSingleton:
                if toappend != "":
                    word.append(toappend)
                word.append(i)
                toappend = ""
            else:
                toappend += i
        if toappend != "":
            word.append(toappend)
        opStack = ["Z0"]
        for i in word:
            if i not in opsSingleton:
                opStack.append("OPERAND")
            else:
                if i == "-" or i == "+":
                    opStack.append(i)
                elif i == "*":
                    if (opStack[-1] == "*"):
                        opStack.pop()
                        opStack.append("**")
                    elif (opStack[-1] == "OPERAND"):
                        opStack.append(i)
                    else:
                        raise Exception(["Invalid expression"])

                elif i == "/":
                    if (opStack[-1] == "/"):
                        opStack.pop()
                        opStack.append("//")
                    elif (opStack[-1] == "OPERAND"):
                        opStack.append(i)
                    else:
                        raise Exception(["Invalid expression"])
                else:
                    if (opStack[-1] == "OPERAND"):
                        opStack.append(i)
                    else:
                        raise Exception(["Invalid expression"])
        if (opStack[-1] != "OPERAND"):
            raise Exception(["Invalid expression"])
        else:
            try:
                for i in word:
                    if i not in opsSingleton:
                        i = i.strip()
                        i = i.replace(")", "")
                        i = i.replace("(", "")
                        if (i.isdigit()):
                            pass
                        else:
                            instValid.check(i)
            except Exception as e:
                raise Exception(["Invalid expression"] + list(e.args)[0])
            else:
                return True                            
    
