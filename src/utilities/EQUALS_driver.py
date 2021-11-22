from EQUALS_FA import FA_equals

FAChecker = FA_equals()
try:
    FAChecker.checkEqual("a = \"horse\"")
    #FAChecker.checkEqual("x = 55anying * -5")
except Exception as e:
    print(e)
else:
    print("Success")