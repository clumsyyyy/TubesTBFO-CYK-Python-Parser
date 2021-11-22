from EQUALS_FA import FA_equals

FAChecker = FA_equals()
try:
    FAChecker.checkEqual("x + 2 = 3")
    #FAChecker.checkEqual("x = 55anying * -5")
except Exception as e:
    print(e)
else:
    print("Success")