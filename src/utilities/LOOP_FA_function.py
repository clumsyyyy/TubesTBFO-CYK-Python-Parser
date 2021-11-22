from CNF_general import CNF_LOOP
from LOOP_FA_varchecker import FA_VALIDFUNVARNAMEC
from CYKCHECKER_general import CYKCHECKCLASS
class FA_function_HELPER:
    def checkBool(self, bool_value):
        if bool_value == "True" or bool_value == "False" or bool_value == "None":
            return True
        else:
            raise Exception(["Not a boolean"])
    def checkString(self, string):
        string = string.strip()
        if len(string) <= 0:
            raise Exception(["Empty string"])
        else:
            if ( string[0] == "\"" and string[-1] == "\"") or (string[0] == "'" and string[-1] == "'"):
                return True
            else:
                raise Exception(["Not a string"])
    def checkInt(self, string):
        if string.isdigit():
            return True
        else:
            raise Exception(["Not an integer"])
    def checkFloat(self, string):
        try:
            float(string)
        except ValueError:
            raise Exception(["Not a float"])
        else:
            return True
    def checkFloatArith(self, str):
        try:
            float(str)
        except ValueError:
            return False
        else:
            return True
    def checkComplexArith(self, str):
        str = str.strip()
        token = []
        compOp = ["+", "-", "/", "*"]
        wordBlock = ""
        for i in str:
            if i in compOp:
                if wordBlock != "":
                    token.append(wordBlock.strip())
                    wordBlock = ""
                token.append(i)
            else:
                wordBlock += i
        if wordBlock != "":
            token.append(wordBlock.strip())
        str = "".join(token)
        try:
            complex(str)
        except ValueError:
            return False
        else:
            return True
    def checkArith(self, string):
            instValid = FA_VALIDFUNVARNAMEC()
            if (string.isdigit() or self.checkFloatArith(string) or self.checkComplexArith(string)):
                return True
            arithOps = ["+", "-", "/", "//", "%", "*", "**", "&", "|", "^"]
            opsSingleton = ["+", "-", "*", "/", "%", "&", "|", "^"]
            openingBracketCount = string.count("(")
            closingBracketCount = string.count(")")
            if (openingBracketCount != closingBracketCount):
                raise Exception(["Non-matching brackets"])
            arithFlag = False
            for i in range(len(arithOps)):
                if arithOps[i] in string:
                    arithFlag = True
                    break
            if (openingBracketCount > 0):
                arithFlag = True
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
                            try:
                                self.checkArgs(parsedWord[i])
                            except:
                                if (self.checkArith(parsedWord[i])):
                                    parsedWord[i] = "VALID"
                                else:
                                    raise Exception(["Invalid expression"])
                            else:
                                parsedWord[i] = "VALID"
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
                    # if (" " in i.strip()):
                    #     opStack.append("INVALID")
                    # else:
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
                for i in word:
                    if i not in opsSingleton:
                        i = i.strip()
                        i = i.replace(")", "")
                        i = i.replace("(", "")
                        if (i.isdigit() or self.checkFloatArith(i) or self.checkComplexArith(i)):
                            pass
                        else:
                            try:
                                self.checkVar(i)
                            except Exception as e:
                                try:
                                    self.checkFunction(i)
                                except Exception as e:
                                    raise Exception(["Invalid expression"])
                                else:
                                    pass
                            else:
                                pass
                return True            
    def checkVar(self, string):
        inst = FA_VALIDFUNVARNAMEC()
        try:
            inst.check(string)
        except Exception as e:
            raise e
        else:
            return True
    def checkCyk(self, rule, str):
        inst = CYKCHECKCLASS()
        return inst.check(rule, str)
    
    def checkArgs(self, str):
        if str == "":
            return True
        else:
            argsInst = CNF_LOOP()
            str = str.strip()
            argStack = ["Z0"]
            argBlock = ""
            for i in str:
                if i == ",":
                    if argBlock.count("]") != argBlock.count("["):
                        argBlock += i
                    elif argBlock.count(")") != argBlock.count("("):
                        argBlock += i
                    else:
                        if argStack[-1] == "Z0":
                            if argBlock == "":
                                raise Exception(["Comma not allowed at the beginning"])
                            else:
                                if argBlock != "":
                                    argStack.append(argBlock)
                                    argBlock = ""
                                argStack.append(",")
                        else:
                            if argBlock != "":
                                argStack.append(argBlock)
                                argBlock = ""
                            argStack.append(",")
                else:
                    argBlock += i
            if argBlock != "":
                argStack.append(argBlock)
            print(argStack)
            allArgs = argStack[1:]
            print(allArgs)
            aalen = len(allArgs)
            for i in range(aalen):
                if (allArgs[i] == ","):
                    continue
                else:
                    tocheck = allArgs[i].strip()
                    try:
                        self.checkVar(tocheck)
                    except Exception as e:
                        try:
                            self.checkString(tocheck)
                        except Exception as e:
                            try:
                                self.checkInt(tocheck)
                            except Exception as e:
                                try:
                                    self.checkFloat(tocheck)
                                except Exception as e:
                                    try:
                                        self.checkArith(tocheck)
                                    except Exception as e:
                                        try:
                                            self.checkFunction(tocheck)
                                        except Exception as e:
                                            try:
                                                self.checkList(tocheck)
                                            except Exception as e:
                                                allArgs[i] = "INVALID"
                                            else:
                                                allArgs[i] = "V"
                                        else:
                                            allArgs[i] = "V"
                                    else:
                                        allArgs[i] = "V"
                                else:
                                    allArgs[i] = "V"
                            else:
                                allArgs[i] = "V"
                        else:
                            allArgs[i] = "V"
                    else:
                        allArgs[i] = "V"
            print(allArgs)
            res = self.checkCyk(argsInst.getArgsRule(), allArgs)
            if (res):
                return True
            else:
                raise Exception(["Invalid arguments"])                
    def checkFunction(self, str):
        str = str.strip()
        wordFun = []
        if str[-1] != ")":
            raise Exception(["Missing closing bracket"])
        else:
            slen = len(str)
            to = 0
            for i in range(slen):
                if str[i] == "(":
                    to = i
                    break
            if to == 0:
                raise Exception(["Missing opening bracket"])
            else:
                wordFun.append(str[:to])
                wordFun.append(str[to+1:slen-1])
                try:
                    self.checkVar(wordFun[0])
                    self.checkArgs(wordFun[1])
                except Exception as e:
                    raise e
                else:
                    return True
    def checkList(self, str):
        str = str.strip()
        if str[0] != "[" or str[-1] != "]":
            raise Exception(["Missing Brackets"])
        else:
            str = str[1:-1]
            try:
                self.checkArgs(str)
            except Exception as e:
                raise Exception(["Invalid List"])
            else:
                return True
            
    def checkForLoop(self, str):
        argsRule = CNF_LOOP()
        word = str.strip().split()
        wlen = len(word)
        tempo = word[wlen-1]
        word[wlen-1] = word[wlen-1][0:-1]
        word.append(tempo[-1])
        word = list(filter(lambda a: a != "", word))
        if (len(word) > 4):
            word[3] = ' '.join(word[3:-1])
            del word[4:-1]
        try:
            self.checkFunction(word[3])
        except Exception as e:
            try:
                self.checkVar(word[3])
            except Exception as e:
                word[3] = "INVALID"
                trig = True
                LatestCatch = e
            else:
                word[3] = "VAR"
        else:
            word[3] = "FUNCALL"
        finally:
            try:
                self.checkVar(word[1])
            except Exception as e:
                word[1] = "INVALID"
                trig = True
                LatestCatch = e
            else:
                word[1] = "VAR"
                if (self.checkCyk(argsRule.getForLoopRule(), word)):
                    return True
                else:
                    if (trig):
                        raise Exception(["Invalid For Loop Statement"] + list(LatestCatch.args)[0])
                        return
                    else:
                        raise Exception(["Invalid For Loop Statement"])
    def checkWhileLoop(self, str):
        argsRule = CNF_LOOP()
        str = str.strip()
        word = (' '.join(str.split())).split(" ")
        if (len(word[-1]) > 1):
            tempo = word[-1]
            word[-1] = word[-1][0:-1]
            word.append(tempo[-1])
        tempblock = ' '.join(word[1:-1])
        word[1] = tempblock
        del word[2:-1]
        print(word)
        tocheck = word[1]
        try:
            self.checkVar(tocheck)
        except:
            try:
                self.checkFunction(tocheck)
            except:
                word[1] = "INVALID"
            else:
                word[1] = "FUNCALL"
        else:
            word[1] = "VAR"
        res = self.checkCyk(argsRule.getWhileLoopRule(), word)
        print(word)
        if (res):
            return True
        else:
            raise Exception(["Invalid While Loop Statement"])





            
                        