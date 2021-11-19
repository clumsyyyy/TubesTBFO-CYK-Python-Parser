import CNF_general as CNF_functionargs
import CYKCHECKER_general as cykcheck
import LOOP_FA_function as FA_function

funVarCheck = FA_function.FA_VALIDFUNVARNAMEC()
argsRule =  CNF_functionargs.CNF_LOOP()
cykChecker = cykcheck.CYKCHECKCLASS()
extractfnargs = FA_function.SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
fa_helper = FA_function.FA_function_HELPER()

try:
    fa_helper.checkforloopstatement("for i in range(5 4, 6, 1):")
except Exception as e:
    print(e.args[0] + ":", e.args[1])
else:
    print("Success")