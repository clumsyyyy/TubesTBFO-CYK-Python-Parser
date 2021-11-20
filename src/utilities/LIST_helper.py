from ARITH_helper import arithHelper
from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER

class listHelper:
    def checkList(self, string):
        lst = string.split(",")
        commaCount = string.count(",")
        for i in range(len(lst)):
            if lst[i] == " ":
                raise Exception("Empty element")

        #reformatting
        for i in range(len(lst)):
            lst[i] = lst[i].replace(" ", "")
            if "[" in lst[i]:
                lst[i] = lst[i].replace("[", "")
            if "]" in lst[i]:
                lst[i] = lst[i].replace("]", "")
            if lst[i].isdigit():
                lst[i] = int(lst[i])
            elif lst[i][0] == "-":
                lst[i] = int(lst[i][1:]) * -1

        checkArith = arithHelper()
        varCheck = FA_VALIDFUNVARNAMEC()
        funcCheck = FA_function_HELPER()
        arithOps = ["+", "-", "/", "//", "%", "*"]
        #cek ada quote yang ga ngepas
        for i in range(len(lst)):
            elmt = str(lst[i])
            if elmt[0] == "\"" and elmt[-1] != "\"":
                raise Exception("Mismatching quote sign")
            #cek fungsi
            elif any(x in arithOps for x in elmt):
                checkArith.checkArithStatement(elmt)
            elif "()" in elmt:
                funcCheck.checkfuncall(elmt)
            elif "\"" not in elmt and not elmt.isdigit():
                try:
                    varCheck.check(elmt)
                except Exception as e:
                    raise e

            # cek dia operasi bukan

        if len(lst) != commaCount + 1:
            raise Exception("Too many commas")

    
listHelp = listHelper()
try:
    listHelp.checkList("[\"-69\", \"cok\", 69*420, mengontol, jancok()]") #mengontol variabel misalnya
except Exception as e:
    print(e)
else:
    print("Success")