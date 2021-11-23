import os
import sys
from CONDITIONAL_parser import conditionalParser
from FREETYPE_parser import freetypeParser
from LOOP_FA_function import FA_function_HELPER
from EQUALS_parser import equalsParser
from IMPORT_parser import checkimp

def checker(path):
    #class instantiations
    loopFuncCheck = FA_function_HELPER()
    conditionals = conditionalParser()
    defcheck = freetypeParser()
    equal = equalsParser()

    #flags
    ifIndent = []
    defIndent = []
    returnIndent = []
    loopIndent = []
    commentStart = False


    # ========== DRIVER ==========
    # print("\nSelamat datang di Another CYK Parser!")
    # print("Silahkan masukkan nama file...\n(pastikan file sudah berada di folder samples)")
    # path = "utilities/samples/" + input(">>> ")

    # while (not os.path.exists(path)):
    #     print("File '", path, "' tidak ada!\n")
    #     print("Silahkan masukkan nama file...\n(pastikan file sudah berada di folder samples)")
    #     path = "utilities/samples/" + input(">>> ")
    path = "samples/" + path
    print("\nMembuka file", path, "...\n")
    if not os.path.exists(path):
        print("File '", path, "' tidak ada!\n")
        
    
    errArr = []
    count = 1
    file = open(path, "r", encoding="utf8")
    lineArr = []
    contextedKeywords = ["break", "continue", "pass"]
    for line in file:
        if line != "\n":
            lineArr.append([line, len(line) - len(line.lstrip())])
    file.close()

    for i in range(len(lineArr)):
        print(len(lineArr[i][0]))
        if lineArr[i][0] != '\n' or len(lineArr[i][0]) != 0:
            expression = lineArr[i][0].strip("\n").strip()
            indent = lineArr[i][1]
            print("Line", count, ": ", end = "")
            print(expression)

            loopIndent = [x for x in loopIndent if x < indent]
            defIndent = [x for x in defIndent if x <= indent]
            returnIndent = [x for x in returnIndent if x <= max(defIndent)]
            
            if expression[0] == "#": #comment
                pass
            elif "#" in expression:
                expression = expression.split("#")[0].strip()
            elif expression[:3] == "\'\'\'" and expression[-3:] == "\'\'\'" and len(expression) != 3:
                continue
            elif expression[:3] == "\'\'\'" or expression[-3:] == "\'\'\'" :
                if commentStart == False:
                    commentStart = True
                    print("comment start")
                elif commentStart == True:
                    commentStart = False
                    print("comment end")
            else:
                if not commentStart:
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
                                                    
                                                    else:
                                                        print("Error in line", count, "->", expression)
                                                        break
                                                else:
                                                    pass
                                                    print("function call")
                                            else:
                                                pass
                                                print("import statement")
                                        else:
                                            pass
                                            print("equal statement")
                                    else:
                                        print("while statement")
                                        loopIndent.append(indent)
                                else:
                                    print("loop statement")
                                    loopIndent.append(indent)
                            else: #cek return
                                if "return" in expression:
                                    if indent not in returnIndent:
                                        returnIndent.append(indent) 
                                    if len(defIndent) != 0:
                                        if indent <= max(defIndent):
                                            print("wrong indentation position for return")
                                            break
                                    else:
                                        print("return not initiated with def")
                                        break
                        else: #cek def
                            print("def statement")
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
                                    print("else statement")
                                    ifIndent = [x for x in ifIndent if x < indent]
                                else:
                                    if lineArr[i + 1][1] > indent:
                                        print("else statement")
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
                                    print("elif statement")
                                else:
                                    if lineArr[i + 1][1] > indent:
                                        print("elif statement")
                                        pass
                                    else:
                                        print("Error in line", count, "->", expression)
                                        print("Error: elif should be followed with a statement")
                                        break
                        elif "if" in expression:
                            try:
                                conditionals.checkConditionals(lineArr[i + 1][0].strip('\n').strip())
                            except:
                                print("if statement")
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
    elif count - 1 == len(lineArr) and not commentStart:
        print("Program accepted!\n")



checker("inputList.py")
