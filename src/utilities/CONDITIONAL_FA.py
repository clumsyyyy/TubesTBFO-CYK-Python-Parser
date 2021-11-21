from BOOL_FA import FA_boolean
from CYKCHECKER_general import CYKCHECKCLASS
from CNF_general import CNF_CONDITIONAL
class FA_conditional:
    def checkConditionals(self, string):
        keyWords = ["if", "elif", "else"]
        # cek colon
        if (string[-1] != ":"):
            raise Exception("Colon sign missing")
        if string.count(":") > 1:
            raise Exception("Too many colon signs")
        #cek apakah bener depannya keyword
        
        arr = (' '.join(string.split())).split(' ')

        if ":" in arr[-1] and arr[-1] != ":":
            arr[-1] = arr[-1][:-1]
            arr.append(":")

        if (arr[0] not in keyWords):
            raise Exception("Missing if/else keyword")
        if (arr[0] == "else") and (arr[1] != ":"):
            raise Exception("else statement wrong")
        statement = ' '.join(arr[1:-1])
        
        bool = FA_boolean()
        try:
            bool.checkBoolStatement(statement)
        except Exception as e:
            try:
                bool.checkComparisonStatement(statement)
            except Exception as e:
                statement = "INVALID"
            else:
                statement = "STATEMENT"
        else:
            statement = "STATEMENT"
        print(statement)

        cyk = CYKCHECKCLASS()
        condRule = CNF_CONDITIONAL()
        if cyk.check(condRule.getNewCondRule(), [arr[0], statement, arr[-1]]):
            return True
        else:
            raise Exception("Incompatible grammar!")