from MISC_parser import MISC_PARSER

Checker = MISC_PARSER()

try:
    Checker.checkDefClass("def   hehe  (   test   ) :")
except Exception as e:
    print(e)
else:
    print("Success")