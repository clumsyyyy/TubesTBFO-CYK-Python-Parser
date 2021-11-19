from BOOL_FA import FA_boolean
from CNF_general import CNF_Boolean
from CYKCHECKER_general import CYKCHECKCLASS

FAChecker = FA_boolean()
try:
    FAChecker.checkBoolStatement("(not True) or (False)") # <- ganti isi string kalo mo tes
    #FAChecker.checkComparisonStatement("(12*-34) < (6 * - 5 // 9)")
except Exception as e:
    print(e)
else:
    print("Success")