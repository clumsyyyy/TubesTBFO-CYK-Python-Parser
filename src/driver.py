from CONDITIONAL_parser import conditionalParser
from FREETYPE_parser import freetypeParser
from LOOP_FA_function import FA_function_HELPER
from EQUALS_parser import equalsParser
from IMPORT_parser import IMPORT_PARSER

loopFuncCheck = FA_function_HELPER()
conditionals = conditionalParser()
defcheck = freetypeParser()
equal = equalsParser()
importCheck = IMPORT_PARSER()

try:
    defcheck.checkPassReturnRaise("return 5 <= 6 and \"a\" in \"makllo\"")
except Exception as e:
    print(e)
else:
    print("success")

