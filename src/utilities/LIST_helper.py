from ARITH_helper import arithHelper
from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER
from CNF_general import CNF_LOOP
class listHelper:
    def checkBool(self, bool_value):
        if bool_value == "True" or bool_value == "False" or bool_value == "None":
            return True
        else:
            return False
    def checkString(self, string):
        doubleQuote = string.count("\"")
        singleQuote = string.count("\'")
        if doubleQuote % 2 != 0 or singleQuote % 2 != 0:
            raise Exception(["Mismatching quote sign"])
        else:
            return True
    def checkInt(self, string):
        if string.isdigit():
            return True
        else:
            raise Exception(["Not an integer"])
    def checkFloat(self, string):
        if "." in string:
            return True
        else:
            raise Exception(["Not a float"])
    def checkArith(self, string):
        inst = arithHelper()
        try:
            inst.checkArithStatement(string)
        except Exception as e:
            raise e
        else:
            return True
    def checkVar(self, string):
        inst = FA_VALIDFUNVARNAMEC()
        try:
            inst.check(string)
        except Exception as e:
            raise e
        else:
            return True

    def checkList(self, string):
        string = string.strip()
        if (string[0] != "[") or (string[-1] != "]"):
            raise Exception(["Not a list"])
        listElinString = string[1:-1]
        listElinString = listElinString.strip()
        if listElinString == "":
            return True
        wordListEl = []
        buf = ""
        for i in listElinString:
            if i == ",":
                wordListEl.append(buf.strip())
                wordListEl.append(i)
                buf = ""
            else: 
                buf += i
        if (buf != ""):
            wordListEl.append(buf.strip())
        print(wordListEl)
        
        arith = arithHelper()
        var = FA_VALIDFUNVARNAMEC()
        func = FA_function_HELPER()
        loopRule = CNF_LOOP.getArgsRule()
        boolC = self.checkBool()
        stringC = self.checkString()
        # integer, string, function, list lain, boolean value, arith, variable



        # for i in range(len(strArr)):
        #     if strArr[i] == ",":
        #         if strArr[i - 1] == "," or strArr[i + 1] == ",":
        #             raise Exception("Too many commas")
        #             break
        # lst = string.split(",")
        
        # commaCount = string.count(",")
        # for i in range(len(lst)):
        #     if lst[i] == " ":
        #         raise Exception("Empty element")
        #         break

        # #reformatting
        # for i in range(len(lst)):
        #     lst[i] = lst[i].replace(" ", "")
        #     if "[" in lst[i]:
        #         lst[i] = lst[i].replace("[", "")
        #     if "]" in lst[i]:
        #         lst[i] = lst[i].replace("]", "")
        #     if lst[i].isdigit():
        #         lst[i] = int(lst[i])
        #     elif lst[i][0] == "-":
        #         lst[i] = int(lst[i][1:]) * -1

        # checkArith = arithHelper()
        # varCheck = FA_VALIDFUNVARNAMEC()
        # funcCheck = FA_function_HELPER()
        # arithOps = ["+", "-", "/", "//", "%", "*"]
        # #cek ada quote yang ga ngepas
        # for i in range(len(lst)):
        #     elmt = str(lst[i])
        #     if elmt[0] == "\"" and elmt[-1] != "\"":
        #         raise Exception("Mismatching quote sign")
        #     #cek fungsi
        #     elif any(x in arithOps for x in elmt):
        #         checkArith.checkArithStatement(elmt)
        #     elif "()" in elmt:
        #         funcCheck.checkfuncall(elmt)
        #     elif "\"" not in elmt and not elmt.isdigit():
        #         try:
        #             varCheck.check(elmt)
        #         except Exception as e:
        #             raise e

        #     # cek dia operasi bukan

        # if len(lst) != commaCount + 1:
        #     raise Exception("Too many commas")
        # else:
        #     return True

listHelp = listHelper()
try:
    listHelp.checkList("[\"-69\", \"cok\", 69*s,, mengontol, [jancok()]]") #mengontol variabel misalnya
except Exception as e:
    print(e)
else:
    print("Success")
