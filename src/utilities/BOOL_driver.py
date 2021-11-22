from BOOL_FA import FA_boolean

FAChecker = FA_boolean()
try:
    #FAChecker.checkBoolStatement("5 and 4") # <- ganti isi string kalo mo tes
    #FAChecker.checkBoolStatement("not abc is kekw")
    FAChecker.checkBoolStatement("True and 8")

    #not True and False or 5
except Exception as e:
    print(e)
else:
    print("Success")