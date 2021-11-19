import sys 
import os

srcfold = "C:\\reverseon\\code\\github\\TubesTBFO\\src\\"
cykpath = "cykcheck\\"
cnfpath = "parser\\loop\\"
sys.path.append(srcfold + cykpath)
sys.path.append(srcfold + cnfpath)

from CNF import CNF_functionargs
from cykchecker import cykcheck

class FA_VALIDFUNVARNAMEC:
    def __init__(self):
        self.res = True

    def _start(self, str) -> bool:
        self.res = True
        if (str == ''):
            self._dead('')
        elif (str[0] == '_' or str[0].isalpha()):
            self._finish(str[1:])
        else:
            self._dead(str[1:])
        return self.res
        
    def _finish(self, str):
        if (str == ''):
            self.res = True
        elif (str[0] == '_' or str[0].isalpha() or str[0].isdigit()):
            self._finish(str[1:])
        else:
            self._dead(str[1:])

    def _dead(self, str):
            raise Exception("Invalid variable/function name")
            self.res = False
            
    def check(self, str):
        return self._start(str)

class FA_function_HELPER:
    def checkargs(self, str) -> bool:
        # STR TO WORD
        if (str == ""):
            return True
        funVarCheck = FA_VALIDFUNVARNAMEC()
        argsRule = CNF_functionargs.CNF_LOOP()
        cykChecker = cykcheck.CYKCHECKCLASS()
        str = str.strip()
        str = ' '.join(str.split())
        word = []
        buf = ""
        for i in str:
            if i == ",":
                word.append(buf.strip())
                word.append(i)
                buf = ""
            else: 
                buf += i
        if (buf != ""):
            word.append(buf.strip())
        # CHECK WORD
        wordlen = len(word)
        for i in range(0, wordlen):
            if (word[i] != ","):
                if (not word[i].isdigit()):
                    try:
                        funVarCheck.check(word[i])
                    except Exception as e:
                        raise e
                        return
                    else:
                        word[i] = "V"
                else:
                    word[i] = "V"

        res = cykChecker.check(argsRule.getArgsRule(), word);
        if (res):
            return True
        else:
            raise Exception("Invalid Function Arguments")
            return 

    def checkfuncall(self, str): 
        # withcolon toggled specific for "for in" call 
        # if variablepermitted is set to true, then input of a variable is permitted, Variable is allowed.
        # such as function(a,b,c) or function(a,b,c): are allowed (later if with colon are enabled) 
        # STR TO WORD
        if (str == ""):
            raise Exception("Invalid Function Call")
            return
        funVarCheck = FA_VALIDFUNVARNAMEC()
        extractfnargs = SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
        str = str.strip()
        word = str.split()
        str = ' '.join(word)
        try:
            res = extractfnargs.extract(str) # VIBECHECK FUNCTION NAME AND ARGS
            funVarCheck.check(res[0])
            self.checkargs(res[2])
        except Exception as e:
            raise e
            return
        else:
            return True

    def checkforloopstatement(self, str):
        # WORD TO STR
        LatestCatch = ""
        funVarCheck = FA_VALIDFUNVARNAMEC()
        cykCheck = cykcheck.CYKCHECKCLASS()
        argsRule = CNF_functionargs.CNF_LOOP()
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
            self.checkfuncall(word[3])
        except Exception as e:
            try:
                funVarCheck.check(word[3])
            except Exception as e:
                word[3] = "INVALID"
                LatestCatch = e
            else:
                word[3] = "VAR"
        else:
            word[3] = "FUNCALL"
        finally:
            try:
                funVarCheck.check(word[1])
            except Exception as e:
                word[1] = "INVALID"
                LatestCatch = e
            else:
                word[1] = "VAR"
                if (cykCheck.check(argsRule.getForLoopRule(), word)):
                    return True
                else:
                    raise Exception("Invalid For Loop Statement", LatestCatch)
                    return



            

class SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES:
    def __init__(self):
        self.fun_name = ''
        self.argsraw = ''
        self.res = False

    def extract(self, str): 
        self.fun_name = ''
        self.argsraw = ''
        self.res = False # Unchanged if Failed
        self._start(str)
        return self.res
    
    def _start(self, str):
        if (str == ''):
            raise Exception("Missing argument")
            return
        elif (str[0] == '('):
            self._extractargs(str[1:])
        else:
            self.fun_name += str[0]
            self._start(str[1:])

    def _extractargs(self, str):
        if (str == ''):
            raise Exception("Missing ')'")
            return
        elif (str[0] == ')'):
            if (len(str) > 1):
                raise Exception("Extra characters after ')'")
                return
            else:
                self._finish()
        else:
            self.argsraw += str[0]
            self._extractargs(str[1:])

    def _finish(self):
        self.res = [self.fun_name.strip(), "(", self.argsraw, ")"]