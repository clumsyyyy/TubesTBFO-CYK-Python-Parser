from LOOP_FA_function import FA_VALIDFUNVARNAMEC
from CYKCHECKER_general import CYKCHECKCLASS
from BOOL_FA import FA_boolean
from CNF_general import CNF_MISC
from LOOP_FA_function import FA_VALIDFUNVARNAMEC


class MISC_PARSER:
    # buat def,class,try,raise,return,pass, di sini
    
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

        #print(arr)
        if (arr[0] not in keyWords):
            raise Exception(["Missing def/class keyword"])
        #if (arr[0] == "else") and (arr[1] != ":"):
        #    raise Exception(["else statement wrong"])

        func = (' '.join(arr[1:-1]))
        #print(func)
        
        varFunChecker = FA_VALIDFUNVARNAMEC()
        if "(" in func:
            if ")" not in func:
                raise Exception(["Missing ')'"])
            else:
                funcName = func[:func.find('(')]
                funcName = funcName.strip()
                #print(funcName)
                if(func.find('(')+1 != func.find(')')):
                    arguments = func[func.find('(')+1:-1]
                    arguments = arguments.split(',')
                    for i in range(len(arguments)):
                        arguments[i]= arguments[i].strip()
                else:
                    arguments = []
                #print(arguments)
                    
                for i in range(len(arguments)):
                    try:
                        varFunChecker.check(arguments[i])
                    except Exception as e:
                        raise(e)
                    else:
                        arguments[i] = "VAR"
                    
                #print(arguments)
        else:
            funcName = func
            arguments = []
        try: 
            varFunChecker.check(funcName)
        except Exception as e:
            raise(e)
        else:
            funcName = "FUNNAME"
                        
        word = [arr[0],funcName]
        word.extend(arguments)
        word.append(arr[-1])
        
        cyk = CYKCHECKCLASS()
        defClassRule = CNF_MISC()
        if cyk.check(defClassRule.getDefClass(), word):
            return True
        else:
            raise Exception(["Incompatible grammar!"])