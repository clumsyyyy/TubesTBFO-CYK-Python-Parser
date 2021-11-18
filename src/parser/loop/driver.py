import sys 
import os


srcfold = "C:\\reverseon\\code\\github\\TubesTBFO\\src\\"
cykpath = "cykcheck\\"
fapath = "parser\\loop\\FA\\"
cnfpath = "parser\\loop\\CNF\\"
sys.path.append(os.path.abspath(srcfold + cykpath))
sys.path.append(os.path.abspath(srcfold + fapath))
sys.path.append(os.path.abspath(srcfold + cnfpath))

from FA_function import *
from CNF_functionargs import *
from cykcheck import *

funVarCheck = FA_VALIDFUNVARNAMEC()
argsRule = CNF_FUNCTIONARGSC()
cykChecker = CYKCHECKCLASS()
extractfnargs = SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
fa_helper = FA_function_HELPER()

def checkforloopstatement(str):
    # WORD TO STR
    word = []
    buf = ""
    strlen = len(str)
    for i in range(0, strlen):
        if (str[i] == " "):
            word.append(buf)
            buf = ""
        else:
            buf += str[i]
    if (buf != ""):
        word.append(buf)
    word = list(filter(lambda a: a != "", word))
    if (word[2] != "in"):
        raise Exception("Error: Invalid loop statement: Unknown keyword")
        return
    elif (word[-1] != ":"):
        if (word[-1][-1] != ":"):
            raise Exception("Missing colon at the end")
            return
        else:
            word[-1] = word[-1][:-1]
            word.append(":")

    print(word)
    word[3] = ''.join(word[3:-1])
    del word[4:]
    print(word)
    try:
        funVarCheck.check(word[1])
    except Exception as e:
        raise e
        return
    else:
        try:
            fa_helper.checkfuncall(word[3], False)
        except Exception as e:
            raise e
            return
        else:
            return True
try:
    checkforloopstatement("for dsa in range(  a,  b, sadas    dsadsa) :")
except Exception as e:
    print(e)
else:
    print("Success")