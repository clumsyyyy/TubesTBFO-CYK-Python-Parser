from EQUALS_FA import FA_equals

FAChecker = FA_equals()
try:
    FAChecker.checkEqual("a = not True")
except Exception as e:
    print(e)
else:
    print("Success")