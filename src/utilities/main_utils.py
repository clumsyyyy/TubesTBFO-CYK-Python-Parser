import os
from CONDITIONAL_FA import FA_conditional
from MISC_parser import MISC_PARSER
from LOOP_FA_function import FA_function_HELPER
from EQUALS_FA import FA_equals
from IMPORT_driver import checkimp
#class instantiazitonsfd
loopFuncCheck = FA_function_HELPER()
conditionals = FA_conditional()
defcheck = MISC_PARSER()
equal = FA_equals()

#flags
ifIndent = []
defIndent = []
returnIndent = []
loopIndent = []
commentStart = False




# ========== DRIVER ==========
print("\nSelamat datang di Another CYK Parser!")
print("Silahkan masukkan nama file...\n(pastikan file sudah berada di folder samples)")
path = "utilities/samples/" + input(">>> ")

while (not os.path.exists(path)):
    print("File '", path, "' tidak ada!\n")
    print("Silahkan masukkan nama file...\n(pastikan file sudah berada di folder samples)")
    path = "utilities/samples/" + input(">>> ")

print("\nMembuka file", path, "...\n")
errArr = []
count = 0
file = open(path, "r", encoding="utf8")
lineArr = []
contextedKeywords = ["break", "continue", "pass"]
for line in file:
    if line != "\n":
        lineArr.append([line, len(line) - len(line.lstrip())])
file.close()

for i in range(len(lineArr)):
    if lineArr[i] != '\n':
        # print("Line", count, ": ", end = "")
        expression = lineArr[i][0].strip("\n").strip()
        indent = lineArr[i][1]
        # print(expression)
        loopIndent = [x for x in loopIndent if x < indent]
        defIndent = [x for x in defIndent if x <= indent]
        returnIndent = [x for x in returnIndent if x <= max(defIndent)]

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
                        loopFuncCheck.checkForLoop(expression)
                    except Exception as e:
                        try:
                            loopFuncCheck.checkWhileLoop(expression)
                        except Exception as e:
                            try:
                                equal.checkEqual(expression)
                            except Exception as e:
                                try:
                                    checkimp(expression)
                                except Exception as e:
                                    try:
                                        loopFuncCheck.checkFunction(expression)
                                    except Exception as e:
                                        if expression in contextedKeywords:
                                            if len(loopIndent) != 0:
                                                if indent > max(loopIndent):
                                                    print(expression)
                                                else:
                                                    print("Error in line", count, "->", expression)
                                                    break
                                            else:
                                                print("Error: no loop initiated")
                                                break
                                        elif expression[0] == "#": #comment
                                            pass
                                        elif expression[2:] == "\'\'\'":
                                            if commentStart == False:
                                                commentStart = True
                                        elif "\'\'\'" in expression:
                                            if commentStart == True:
                                                commentStart = False
                                        else:
                                            print("Error in line", count, "->", expression)
                                            break
                                    else:
                                        pass
                                        # print("function call")
                                else:
                                    pass
                                    #print("import statement")
                            else:
                                pass
                                #print("equal statement")
                        else:
                            #print("while statement")
                            loopIndent.append(indent)
                    else:
                        print("loop statement")
                        loopIndent.append(indent)
                else: #cek return
                    if "return" in expression:
                        if indent not in returnIndent:
                            returnIndent.append(indent) 
                        if indent <= max(defIndent):
                            print("wrong indentation position for return")
                            break
            else: #cek def
                #print("def statement")
                if indent not in defIndent:
                    defIndent.append(indent)
        else: #cek indentasi if else
            if "else" in expression:
                if indent not in ifIndent:
                    print("Error in line", count, "->", expression)
                    print("Error: else initiated before if")
                    break
                else:
                    try:
                        conditionals.checkConditionals(lineArr[i + 1][0].strip('\n').strip())
                    except Exception as e:
                        #print("else statement")
                        ifIndent = [x for x in ifIndent if x < indent]
                    else:
                        if lineArr[i + 1][1] > indent:
                            #print("else statement")
                            print(indent)
                            ifIndent = [x for x in ifIndent if x < indent]
                        elif indent not in ifIndent:
                            print("Error in line", count, "->", expression)
                            print("Error: else should be followed with a statement")
                            break
            elif "elif" in expression:
                if indent not in ifIndent:
                    print("Error in line", count, "->", expression)
                    print("Error: elif initiated before if")
                    break
                else:
                    try:
                        conditionals.checkConditionals(lineArr[i + 1][0].strip('\n').strip())
                    except:
                        pass
                        #print("elif statement")
                    else:
                        if lineArr[i + 1][1] > indent:
                            #print("elif statement")
                            pass
                        else:
                            print("Error in line", count, "->", expression)
                            print("Error: elif should be followed with a statement")
                            break
            elif "if" in expression:
                try:
                    conditionals.checkConditionals(lineArr[i + 1][0].strip('\n').strip())
                except:
                    #print("if statement")
                    if indent not in ifIndent:
                        ifIndent.append(indent)
                else:
                    if lineArr[i + 1][1] >= indent:
                        #print("if statement")
                        if indent not in ifIndent:
                            ifIndent.append(indent)
                        if lineArr[i + 1][1] not in ifIndent:
                            ifIndent.append(lineArr[i + 1][1])
                    else:
                        print("Error in line", count, "->", expression)
                        print("Error: if should be followed with a statement")
                        break    
        # # evaluasi tiap line

        count += 1

if commentStart:
    print("Comment started but not ended")
if count == len(lineArr):
    print("Program accepted!\n")

