from BOOL_FA import FA_boolean

FAChecker = FA_boolean()
try:
    FAChecker.checkBoolStatement("x * 3 <= 40 and maklo == True") # <- ganti isi string kalo mo tes
    #FAChecker.checkBoolStatement("not abc is kekw")
    FAChecker.checkBoolStatement("True and 8")

    #not True and False or 5
except Exception as e:
    print(e)
else:
    print("Success")