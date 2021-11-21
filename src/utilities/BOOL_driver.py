from BOOL_FA import FA_boolean

FAChecker = FA_boolean()
try:
    FAChecker.checkBoolStatement("(not 5) and teeteed and maklo()") # <- ganti isi string kalo mo tes
    #FAChecker.checkBoolStatement("not abc is kekw")
    #FAChecker.checkComparisonStatement("2 * (--3)!=6")
except Exception as e:
    print(e)
else:
    print("Success")