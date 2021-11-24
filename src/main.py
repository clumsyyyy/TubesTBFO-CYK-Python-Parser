import os
import sys
from CONDITIONAL_parser import conditionalParser
from FREETYPE_parser import freetypeParser
from LOOP_FA_function import FA_function_HELPER
from EQUALS_parser import equalsParser
from IMPORT_parser import IMPORT_PARSER

def checker(path):
    #class instantiations
    loopFuncCheck = FA_function_HELPER()
    conditionals = conditionalParser()
    defcheck = freetypeParser()
    equal = equalsParser()
    importCheck = IMPORT_PARSER()

    #flags
    ifIndent = []
    defIndent = []
    returnIndent = []
    loopIndent = []
    commentStart = False
    errFlag = False
    path = "samples/" + path
    print("\nOpening file", path, "...\n")
    if not os.path.exists(path):
        print("File '", path, "' tidak ada!\n")
        
    
    errArr = []
    count = 0
    file = open(path, "r", encoding="utf8")
    lineArr = []
    contextedKeywords = ["break", "continue", "pass"]
    for line in file:
        if line != "\n" or line != "":
            lineArr.append([line, len(line) - len(line.lstrip())])
    file.close()

    for i in range(len(lineArr)):
        count += 1
        if lineArr[i][0] != "\n":
            expression = lineArr[i][0].strip("\n").strip()
            indent = lineArr[i][1]
            # print("Line", count, ": ", end = "")
            # print(expression)
            loopIndent = [x for x in loopIndent if x < indent]
            defIndent = [x for x in defIndent if x < indent]
            if len(defIndent) != 0:
                returnIndent = [x for x in returnIndent if x <= max(defIndent)]
            else:
                returnIndent = []
            if expression[0] == "#" and len(expression) > 0: #comment
                continue
            elif "#" in expression:
                expression = expression.split("#")[0].strip()
                #print(expression)
            elif expression[:3] == "\'\'\'" and expression[-3:] == "\'\'\'" and len(expression) != 3:
                continue
            elif expression[:3] == "\'\'\'" or expression[-3:] == "\'\'\'" :
                if commentStart == False:
                    commentStart = True
                    #print("comment start")
                elif commentStart == True:
                    commentStart = False
                    #print("comment end")

            if not commentStart and (expression[:3] != "\'\'\'" and expression[-3:] != "\'\'\'"):
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
                                            importCheck.checkimp(expression)
                                        except Exception as e:
                                            try:
                                                loopFuncCheck.checkFunction(expression)
                                            except Exception as e:
                                                if expression in contextedKeywords:
                                                    if len(loopIndent) != 0:
                                                        if indent > max(loopIndent):
                                                            pass
                                                            #print(expression)
                                                        else:
                                                            print('\033[93m' + "Syntax Error in line", count, ": ", expression)
                                                            errFlag = True
                                                            break
                                                    else:
                                                        print('\033[93m' + "Error in line", count, ": ", expression)
                                                        print('\033[93m' + "Error: no loop initiated for context keywords (break/continue/pass)")
                                                        errFlag = True
                                                        break
                                                
                                                else:
                                                    print('\033[93m' + "Syntax Error in line", count, ": ", expression)
                                                    errFlag = True
                                                    break
                                            else:
                                                pass
                                                #print("function call")
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
                                #print("loop statement")
                                loopIndent.append(indent)
                        else: #cek return
                            if "return" in expression:
                                if indent not in returnIndent:
                                    returnIndent.append(indent) 
                                if len(defIndent) != 0:
                                    if indent <= max(defIndent):
                                        print('\033[93m' + "Error in line", count, ": ", expression)
                                        print('\033[93m' + "wrong indentation position for return")
                                        errFlag = True
                                        break
                                else:
                                    print('\033[93m' + "Error in line", count, ": ", expression)
                                    print('\033[93m' + "return not initiated with def")
                                    errFlag = True
                                    break
                    else: #cek def
                        #print("def statement")
                        if indent not in defIndent:
                            defIndent.append(indent)
                else: #cek indentasi if else
                    #print("conditionals")
                    if "else" in expression:
                        if indent not in ifIndent:
                            print('\033[93m' + "Error in line", count, ": ", expression)
                            print('\033[93m' + "Error: else initiated before if")
                            errFlag = True
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
                                    ifIndent = [x for x in ifIndent if x < indent]
                                elif indent not in ifIndent:
                                    print('\033[93m' + "Error in line", count, ": ", expression)
                                    print('\033[93m' + "Error: else should be followed with a statement")
                                    errFlag = True
                                    break
                    elif "elif" in expression:
                        if indent not in ifIndent:
                            print('\033[93m' + "Error in line", count, ": ", expression)
                            print('\033[93m' + "Error: elif initiated before if")
                            errFlag = True
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
                                    print('\033[93m' + "Error in line", count, ": ", expression)
                                    print('\033[93m' + "Error: elif should be followed with a statement")
                                    errFlag = True
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
                                print('\033[93m' + "Error in line", count, ": ", expression)
                                print('\033[93m' + "Error: if should be followed with a statement")
                                errFlag = True  
                                break
                # # evaluasi tiap line
                    

    if commentStart:
        print("Comment started but not ended")
    elif not errFlag and not commentStart:
        print('\033[92m' + "Program accepted!")
    print('\033[0m')


checker(sys.argv[1])
