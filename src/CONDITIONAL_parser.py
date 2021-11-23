from LOOP_FA_function import FA_function_HELPER
from CYKcheck import CYKCHECKCLASS
from CNF import CNF_CONDITIONAL
class conditionalParser:
    def checkConditionals(self, string):
        keyWords = ["if", "elif", "else", "while"]
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
            raise Exception(["Missing if/else/while keyword"])
        if (arr[0] == "else") and (arr[1] != ":"):
            raise Exception(["else statement wrong"])
        statement = ' '.join(arr[1:-1])
        
        bool = FA_function_HELPER()
        if len(arr) != 2:
            try:
                bool.checkBool(statement)
            except Exception as e:
                try:
                    bool.checkComparison(statement)
                except Exception as e:
                    statement = "INVALID"
                    raise e
                else:
                    statement = "STATEMENT"
            else:
                statement = "STATEMENT"


        cyk = CYKCHECKCLASS()
        condRule = CNF_CONDITIONAL()
        if cyk.check(condRule.getCondRule(), [arr[0], statement, arr[-1]]):
            return True
        else:
            raise Exception(["Incompatible grammar!"])