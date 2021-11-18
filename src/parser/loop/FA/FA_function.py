import sys 
import os

srcfold = "C:\\reverseon\\code\\github\\TubesTBFO\\src\\"
cykpath = "cykcheck\\"
cnfpath = "parser\\loop\\CNF\\"
sys.path.append(os.path.abspath(srcfold + cykpath))
sys.path.append(os.path.abspath(srcfold + cnfpath))

from CNF_functionargs import *
from cykcheck import *

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
        argsRule = CNF_FUNCTIONARGSC()
        cykChecker = CYKCHECKCLASS()
        str = ''.join(str.split())
        word = []
        buf = ""
        for i in str:
            if i == ",":
                word.append(buf)
                word.append(i)
                buf = ""
            else: 
                buf += i
        if (buf != ""):
            word.append(buf)
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

        res = cykChecker.check(argsRule.get(), word);
        if (res):
            return True
        else:
            raise Exception("Invalid Function Arguments")
            return 

    def checkfuncall(self, str, variablePermitted): 
        # withcolon toggled specific for "for in" call 
        # if variablepermitted is set to true, then input of a variable is permitted, Variable is allowed.
        # such as function(a,b,c) or function(a,b,c): are allowed (later if with colon are enabled) 
        # STR TO WORD
        extractfnargs = SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
        str = ''.join(str.split())
        if (str == ""):
            raise Exception("Invalid Function Call")
            return
        try:
            res = extractfnargs.extract(str) # VIBECHECK FUNCTION NAME AND ARGS
        except Exception as e:
            raise e
            return
        else:
            if (not variablePermitted):
                if (res[1] == ""):
                    raise Exception("Missing Parentheses")
                    return
            return True

            

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
            self._questions() # SPECIAL CASE
        elif (str[0] == '('):
            varChecker = FA_VALIDFUNVARNAMEC()
            try:
                varChecker.check(self.fun_name)
            except Exception as e:
                raise e
            else:
                self._extractargs(str[1:])
        else:
            self.fun_name += str[0]
            self._start(str[1:])
        
    def _questions(self):
        if (self.fun_name == ''):
            raise Exception("Missing argument")
            return
        else:
            varChecker = FA_VALIDFUNVARNAMEC()
            try:
                varChecker.check(self.fun_name)
            except Exception as e:
                raise e
                return
            else:
                self.res = [self.fun_name, "", "", ""] # then self.fun_name is actually a variable

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
        try:
            helper = FA_function_HELPER()
            helper.checkargs(self.argsraw)
        except Exception as e:
            raise e
            return
        else:
            self.res = [self.fun_name, "(", self.argsraw, ")"]