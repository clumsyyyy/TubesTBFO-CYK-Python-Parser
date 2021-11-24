from CONDITIONAL_parser import conditionalParser
from FREETYPE_parser import freetypeParser
from LOOP_FA_function import FA_function_HELPER
from EQUALS_parser import equalsParser


loopFuncCheck = FA_function_HELPER()
conditionals = conditionalParser()
defcheck = freetypeParser()
equal = equalsParser()

from IMPORT_parser import IMPORT_PARSER
importCheck = IMPORT_PARSER()
try:
    #conditionals.checkConditionals("if selisih_a == arr_a[i + 1] - arr_a[i] and selisih_b == arr_b[i + 1] - arr_b[i]:")
    #loopFuncCheck.checkComparison("a[i] + a[i - 1]==selisih")
    #loopFuncCheck.checkListElCall("arr[i-1]")
    #loopFuncCheck.checkBool("selisih_a == arr_a[i + 1] - arr_a[i] and selisih_b == arr_b[i + 1] - arr_b[i]")
    #loopFuncCheck.checkComparison("arr_a[j + 1] - arr_a[i] == selisih_a")
    defcheck.checkPassReturnRaise("return ")
except Exception as e:
    print(e)
else:
    print("success")

