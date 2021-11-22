from MISC_parser import MISC_PARSER

Checker = MISC_PARSER()

try:
    Checker.checkPassReturnRaise("raise Exception()")
except Exception as e:
    print(e)
else:
    print("Success")