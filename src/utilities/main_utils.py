import os
from CONDITIONAL_FA import FA_conditional
from MISC_parser import MISC_PARSER
from LOOP_FA_function import FA_function_HELPER
from EQUALS_FA import FA_equals
from IMPORT_driver import checkimp
#class instantiazitonsfd
loopcheck = FA_function_HELPER()
conditionals = FA_conditional()
defcheck = MISC_PARSER()
loopcheck = FA_function_HELPER()
equal = FA_equals()

#flags
ifFlag = False
defFlag = False


# ========== DRIVER ==========
# path = input("Masukkan nama file...\n>>> ")

# while (not os.path.exists(path)):
#     print("File '", path, "' tidak ada!\n")
#     path = input("Masukkan nama file...\n>>> ")

# print("Membuka file", path, "...")
errArr = []
count = 0
file = open("input1.py", "r", encoding="utf8")
lineArr = []
for line in file:
    lineArr.append(line)
file.close()

for i in range(len(lineArr)):
    if lineArr[i] != "\n":
        print("Line", count, ": ", end = "")
        expression = lineArr[i].strip('\n').strip()
        print(expression)
        
        try:
            conditionals.checkConditionals(expression)
        except Exception as e:
            try:
                defcheck.checkDefClass(expression)
            except Exception as e:
                try:
                    defcheck.checkPassReturnRaise(expression)
                except Exception as e:
                    try:
                        loopcheck.checkForLoop(expression)
                    except Exception as e:
                        try:
                            equal.checkEqual(expression)
                        except Exception as e:
                            try:
                                checkimp(expression)
                            except Exception as e:
                                print("Error in line", count)
                                break
                            else:
                                print("import statement")
                        else:
                            print("equal statement")
                    else:
                        print("loop statement")
                else:
                    if "return" in expression and defFlag == True:
                        print("return statement")
                        defFlag = False
                    else:
                        print("Error in line", count)
                        print("'return' initiated without def")
                        break
            else:
                if defFlag == False:
                    defFlag = True
                    print("def statement")
                else:
                    defFlag = False
        else:
            if "if" in expression:
                print("if/else statement")
                ifFlag = True
            elif "else" in expression:
                if ifFlag == False:
                    print("Error: else initiated before if")
                    break
                else:
                    try:
                        conditionals.checkConditionals(lineArr[i - 1].strip('\n').strip())
                    except Exception as e:
                        pass
                    else:
                        print("else should be followed by a statement")
                        ifFlag = False
                        break
            elif "elif" in expression:
                if ifFlag == False:
                    print("Error: elif initiated before if")
                    break


        # # evaluasi tiap line
        print("\n")
        count += 1


