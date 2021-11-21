from CONDITIONAL_FA import FA_conditional

FAChecker = FA_conditional()

try:
    FAChecker.checkConditionals("if x == 0:")
except Exception as e:
    print(e)
else:
    print("Success")