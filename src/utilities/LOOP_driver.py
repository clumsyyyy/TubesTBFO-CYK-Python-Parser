import CNF_general as CNF_functionargs
import CYKCHECKER_general as cykcheck
import LOOP_FA_varchecker as VARCHECK
import LOOP_FA_function as FA_function

varCheck = VARCHECK.FA_VALIDFUNVARNAMEC()
argsRule =  CNF_functionargs.CNF_LOOP()
cykChecker = cykcheck.CYKCHECKCLASS()
fa_helper = FA_function.FA_function_HELPER()

try:
    fa_helper.checkWhileLoop("while file(2^7+(fun(12s24, 3)), b(puopen, 2**263j)) dsa:")
except Exception as e:
    print(e)
else:
    print("Success")