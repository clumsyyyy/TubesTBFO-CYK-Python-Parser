from CONDITIONAL_FA import FA_conditional

FAChecker = FA_conditional()

try:
    FAChecker.checkConditionals("elif 69 == 40 and maklo  + 5s == NONE:")
except Exception as e:
    print(e)
else:
    print("Success")