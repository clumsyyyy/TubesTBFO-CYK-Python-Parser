from CONDITIONAL_FA import FA_conditional

FAChecker = FA_conditional()

try:
    FAChecker.checkConditionals("elif 69 == 40 and maklo  + 5 // 3 ** 2 == NONE:")
except Exception as e:
    print(e)
else:
    print("Success")