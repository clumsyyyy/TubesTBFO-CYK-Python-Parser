import sys
sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")

from cykchecker import cykcheck
from FA import FA_function
from CNF import CNF_functionargs

funVarCheck = FA_function.FA_VALIDFUNVARNAMEC()
argsRule =  CNF_functionargs.CNF_FUNCTIONARGSC()
cykChecker = cykcheck.CYKCHECKCLASS()
extractfnargs = FA_function.SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
fa_helper = FA_function.FA_function_HELPER()

try:
    fa_helper.checkforloopstatement("while True u:")
except Exception as e:
    print(e)
else:
    print("Success")