from CONDITIONAL_FA import FA_conditional

FAChecker = FA_conditional()

try:

    FAChecker.checkConditional("if (True and False) :")
except Exception as e:
    print(e)
else:
    print("Success")


