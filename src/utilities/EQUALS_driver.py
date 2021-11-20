from EQUALS_FA import FA_equals

FAChecker = FA_equals()
try:
    FAChecker.checkEqual("a = [\"-69\", \"cok\", 69*420, mengontol, jancok()]")
except Exception as e:
    print(e)
else:
    print("Success")