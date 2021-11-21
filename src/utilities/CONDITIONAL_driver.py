from CONDITIONAL_FA import FA_conditional

FAChecker = FA_conditional()
try:
    FAChecker.checkConditional("if (1) :")
except Exception as e:
    print(e)
else:
    print("Success")