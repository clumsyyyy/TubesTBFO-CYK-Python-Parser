from CNF import CNF_LOOP
from FA_varchecker import FA_VALIDFUNVARNAMEC
from CYKcheck import CYKCHECKCLASS
class FA_function_HELPER:
    def checkComparison(self, str):
        comparisonOps = [ "<=", ">=", ">", "<", "==", "!="]
        opsCount = 0;
        for i in range(len(comparisonOps)):
            if (comparisonOps[i] in str):
                opsCount += 1
                word = str.split(comparisonOps[i])
                break
        if (opsCount == 0):
            raise Exception(["No comparison operator"])
        else:
            for i in word:
                i = i.strip()
                try:
                    self.checkInt(i)
                except:
                    try:
                        self.checkFloat(i)
                    except:
                        try:
                            self.checkVar(i)
                        except:
                            try:
                                self.checkFunction(i)
                            except:
                                try:
                                    self.checkBool(i)
                                except:
                                    try:
                                        self.checkArith(i)
                                    except:
                                        try:
                                            self.checkComparison(i)
                                        except:
                                            raise Exception(["Invalid comparison"])
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            return True
    def findIndexwithoutHandling(self, arr, target):
        try:
            res = arr.index(target)
        except:
            return -1
        else:
            return res
    def checkBool(self, str):
        str = str.strip()
        argsRule = CNF_LOOP()
        logicOp = ["and", "or", "not"]
        if (str.count("(") != str.count(")")):
            raise Exception(["Missing Brackets"])
        else:
            if (str.count("(") > 0): # there are parentheses
                word = []
                toappend = ""
                for i in str:
                    if i in ["(", ")"]:
                        if toappend != "":
                            word.append(toappend)
                            toappend = ""
                        word.append(i)
                    else:
                        toappend += i
                if toappend != "":
                    word.append(toappend)
                f = True
                parsedWord = []
                wslen = len(word)
                openInsideFirstBracket = 0
                insideapp = ""
                for i in range(wslen):
                    if word[i] == "(":
                        if f:
                            f = False
                            parsedWord.append(word[i])
                        else:
                            openInsideFirstBracket += 1
                            insideapp += word[i]
                    elif word[i] == ")":
                        if openInsideFirstBracket == 0:
                            parsedWord.append(insideapp)
                            parsedWord.append(word[i])
                            insideapp = ""
                            f = True
                        else:
                            openInsideFirstBracket -= 1
                            insideapp += word[i]
                    else:
                        if (f == True):
                            parsedWord.append(word[i])
                        else:
                            insideapp += word[i]
                pwlen = len(parsedWord)
                exprFlag = False
                delFirst = False
                print("parsedbef:", parsedWord)
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
                                try:
                                    self.checkBool(parsedWord[i])
                                except:
                                    parsedWord[i] = "-INVALID-"
                                else:
                                    parsedWord[i] = "BOOLOPS"
                            else:
                                strcheck = parsedWord[i-2]
                                wordCheck = strcheck.split(" ")
                                andpos = self.findIndexwithoutHandling(wordCheck, "and")
                                orpos = self.findIndexwithoutHandling(wordCheck, "or")
                                notpos = self.findIndexwithoutHandling(wordCheck, "not")
                                latestpos = max(andpos, orpos, notpos)
                                if (latestpos != -1):
                                    del wordCheck[latestpos+1]
                                    parsedWord[i-2] = " ".join(wordCheck)
                                else:
                                    delFirst = True
                                parsedWord[i] = "BOOLOPS"
                if (delFirst == True):
                    del parsedWord[0]
                print("parsedaft:", parsedWord)
                parsedWord = list(filter(lambda a: a != "(" and a != ")", parsedWord))
                strIncheck = " ".join(parsedWord)
                res = self.checkBool(strIncheck)
                if (res):
                    return True
                else:
                    raise Exception(["Invalid Boolean Expression"])
            else:
                oldWord = str.split()
                word = []
                wordBlock = ""
                for i in oldWord:
                    if i in logicOp:
                        if wordBlock != "":
                            word.append(wordBlock.strip())
                            wordBlock = ""
                        word.append(i)
                    else:
                        wordBlock += i
                if wordBlock != "":
                    word.append(wordBlock.strip())
                    wordBlock = ""
                print("basecasebef: ", str, word)
                for i in range(len(word)):
                    if word[i] not in ["and", "or", "not"]:
                        if (word[i] == "True" or word[i] == "False" or word[i] == "None"):
                            word[i] = word[i]
                        else:
                            try:
                                self.checkInt(word[i])
                            except:
                                try:
                                    self.checkVar(word[i])
                                except:
                                    try:
                                        self.checkFunction(word[i])
                                    except:
                                        try: 
                                            self.checkComparison(word[i])
                                        except:
                                            raise Exception(["Invalid Boolean Expression"])
                                        else:
                                            word[i] = "COMP"
                                    else:
                                        word[i] = "FUNCALL"
                                else:
                                    word[i] = "VAR"
                            else:
                                word[i] = "INT"
                print("basecaseaft: ",  word)
                res = self.checkCyk(argsRule.getBoolRule(), word)
                if (res):
                    return True
                else:
                    raise Exception(["Invalid boolean"])
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
                                    try:
                                        self.checkList(i)
                                    except:
                                        try:
                                            self.checkBool(i)
                                        except:
                                            raise Exception(["Invalid expression"])
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                return True   
    def checkListElCall(self, str):
        strictlyVar = FA_VALIDFUNVARNAMEC()
        getArgs = CNF_LOOP()
        str = str.strip()
        if (str.count("]") != str.count("[") or str.count("[") <= 0):
            raise Exception(["Invalid list element call"])
        else:
            word = []
            toappend = ""
            for i in str:
                if i in ["[", "]"]:
                    if toappend != "":
                        word.append(toappend)
                        toappend = ""
                    word.append(i)
                else:
                    toappend += i
            try:
                strictlyVar.check(word[0])
            except Exception as e:
                word[0] = "INVALID"
                print(word)
            else:
                word[0] = "VAR"
                wlen = len(word)
                for i in range(1, wlen):
                    if word[i] not in ["[", "]"]:
                        if word[i].isdigit():
                            word[i] = "NUM"
                        else:
                            try:
                                strictlyVar.check(word[i])
                            except:
                                try:
                                    self.checkBool(word[i])
                                except:
                                    try:
                                        self.checkArith(word[i])
                                    except:
                                        try:
                                            self.checkFunction(word[i])
                                        except:
                                            word[i] = "INVALID"
                                        else:
                                            word[i] = "FUNCALL"
                                    else:
                                        word[i] = "ARITH"
                                else:
                                    word[i] = "BOOL"
                            else:
                                word[i] = "VAR"
                res = self.checkCyk(getArgs.getListElRule(), word)
                if (res):
                    return True
                else:
                    raise Exception(["Invalid list element call"])

    def checkVar(self, string): #can accept array too
        inst = FA_VALIDFUNVARNAMEC()
        try:
            inst.check(string)
        except Exception as e:
            try:
                self.checkListElCall(string)
            except Exception as e:
                raise e
            else:
                return True
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
                                        self.checkComparison(tocheck)
                                    except:
                                        try:
                                            self.checkBool(tocheck)
                                        except:
                                            try:
                                                self.checkArith(tocheck)
                                            except Exception as e:
                                                try:
                                                    self.checkFunction(tocheck)
                                                except Exception as e:
                                                    try:
                                                        self.checkList(tocheck)
                                                    except Exception as e:
                                                        pass
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
                        else:
                            allArgs[i] = "V"
                    else:
                        allArgs[i] = "V"
                    finally:
                        if allArgs[i] == "V":
                            continue
                        else:
                            try:
                                self.checkBool(tocheck)
                            except:
                                raise Exception(["Invalid argument"])
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
        if (word[0] != "for"):
            raise Exception(["Invalid for loop"])
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

        tocheck = word[1]
        tocheck = tocheck.strip()
        try:
            self.checkInt(tocheck)
        except:
            try:
                self.checkVar(tocheck)
            except:
                try:
                    self.checkFunction(tocheck)
                except:
                    try:
                        self.checkBool(tocheck)
                    except:
                        try:
                            self.checkArith(tocheck)
                        except:
                            try:
                                self.checkComparison(tocheck)
                            except:
                                raise Exception(["Invalid While Loop Statement"])
                            else:
                                word[1] = "VAR"
                        else:
                            word[1] = "VAR"
                    else:
                        word[1] = "VAR"
                else:
                    word[1] = "FUNCALL"
            else:
                word[1] = "VAR"
        else:
            word[1] = "VAR"
        res = self.checkCyk(argsRule.getWhileLoopRule(), word)

        if (res):
            return True
        else:
            raise Exception(["Invalid While Loop Statement"])
    





            
                        