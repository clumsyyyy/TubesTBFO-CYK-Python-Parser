from BOOL_FA import FA_boolean

FAChecker = FA_boolean()
try:
    #FAChecker.checkBoolStatement("(not True) and teeteed") # <- ganti isi string kalo mo tes
    FAChecker.checkBoolStatement("not abc is not y")
    #FAChecker.checkComparisonStatement("(12*-1*maklo) != (6 * - 5 // 9)")
except Exception as e:
    print(e)
else:
    print("Success")