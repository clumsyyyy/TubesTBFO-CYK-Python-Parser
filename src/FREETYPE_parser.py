from CYKcheck import CYKCHECKCLASS
from CNF import CNF_Freetype
from FA_varchecker import varNameChecker
from LOOP_FA_function import FA_function_HELPER

class freetypeParser:    
    def checkDefClass(self, string):
        # def class di sini
        keyWords = ["def", "class"]
        # cek colon
        if (string[-1] != ":"):
            raise Exception(["Colon sign missing"])
        if string.count(":") > 1:
            raise Exception(["Too many colon signs"])
        #cek apakah bener depannya keyword
        
        arr = (' '.join(string.split())).split(' ')
        if ":" in arr[-1] and arr[-1] != ":":
            arr[-1] = arr[-1][:-1]
            arr.append(":")


        if (arr[0] not in keyWords):
            raise Exception(["Missing def/class keyword"])

        func = (' '.join(arr[1:-1]))

        varFunChecker = varNameChecker()
        funcCheck = FA_function_HELPER()

        try: 
            funcCheck.checkFunction(func)
        except Exception as e:
            raise(e)
        else:
            func = "FUNNAME"
                        
        word = [arr[0],func]

        word.append(arr[-1])
        print(word)
        cyk = CYKCHECKCLASS()
        defClassRule = CNF_Freetype()
        if cyk.check(defClassRule.getDefClass(), word):
            return True
        else:
            raise Exception(["Incompatible grammar!"])
    
    def checkPassReturnRaise(self,string):
        funcallCheck = FA_function_HELPER()
        word = (' '.join(string.split())).split(' ')
        if ":" in word[-1] and word[-1] != ":":
            word[-1] = word[-1][:-1]
            word.append(":")

        if word[-1] == ":":
            raise Exception(["Colon detected at the end of statement"])
        if(word[0] == "return"):
            if (len(word) == 1):
                raise Exception(["return nothing"])
            else:
                statement = ' '.join(word[1:])
                bool = FA_function_HELPER()
                checker =  FA_function_HELPER()
                var = varNameChecker()
                try:
                    bool.checkBool(statement)
                except Exception as e:
                    try:
                        bool.checkComparison(statement)
                    except Exception as e:
                        try:
                            checker.checkString(statement)
                        except Exception as e:
                            try:
                                checker.checkInt(statement)
                            except Exception as e:
                                try:
                                    checker.checkList(statement)
                                except Exception as e:
                                    try:
                                        var.check(statement)
                                    except Exception as e:
                                        statement = "INVALID"
                                    else:
                                        statement = "VAR"
                                else:
                                    statement = "LIST"
                            else:
                                statement = "INT"
                        else:
                            statement = "STRING"
                    else:
                        statement = "STATEMENT"
                else:
                    statement = "STATEMENT"
            word = [word[0],statement]

        elif (word[0] == "raise"):
            checker =  FA_function_HELPER()
            exception = ' '.join(word[1:])
            if len(exception) < 9:
                raise Exception(["No Exception"])
            else:
                if exception[:9] != "Exception":
                    raise Exception(["No Exception"])
                else:
                    try:
                        checker.checkFunction(exception)
                    except Exception as e:
                        raise(e)
                    else:
                        exception = "EXCEPTION"
                        word = [word[0],exception]
        print(word)
        cyk = CYKCHECKCLASS()
        returnRule = CNF_Freetype()
        print(returnRule.getPassReturnRaise())
        if cyk.check(returnRule.getPassReturnRaise(),word):
            return True
        else:
            raise Exception(["Incompatible grammar!"])
        