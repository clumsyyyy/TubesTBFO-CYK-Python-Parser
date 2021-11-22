import CNF_general as CNF_functionargs
import CYKCHECKER_general as cykcheck
import LOOP_FA_varchecker as VARCHECK
import LOOP_FA_function as FA_function

varCheck = VARCHECK.FA_VALIDFUNVARNAMEC()
argsRule =  CNF_functionargs.CNF_LOOP()
cykChecker = cykcheck.CYKCHECKCLASS()
fa_helper = FA_function.FA_function_HELPER()

def checkComparisonStatement(str):
        comparisonOps = [ "<=", ">=", ">", "<", "==", "!="]
        opsCount = 0;
        for i in range(len(comparisonOps)):
            if (comparisonOps[i] in str):
                opsCount += 1
                word = str.split(comparisonOps[i])
                break
        if (opsCount == 0):
            raise Exception(["No comparison operator"])
        if (opsCount > 1):
            raise Exception(["More than one comparison operator detected"])
        #cek arithmetic
        instArith = FA_function.FA_function_HELPER()
        var = VARCHECK.FA_VALIDFUNVARNAMEC()
        for i in range(len(word)):
            if not word[i].replace(" ", "").isdigit():
                try:
                    instArith.checkArith(word[i].replace(" ", ""))
                except Exception as e:
                    try:
                        var.check(word[i].replace(" ", ""))
                    except Exception as e:
                        raise e

try:
    fa_helper.checkForLoop("for x+2=3")
except Exception as e:
    print(e)
else:
    print("Success")