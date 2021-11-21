from LOOP_FA_function import FA_VALIDFUNVARNAMEC
from CYKCHECKER_general import CYKCHECKCLASS
from BOOL_FA import FA_boolean

class FA_conditional:
    def checkConditional(self,str):
        if "if" not in str and "else" not in str and "elif" not in str:
            raise Exception("Tidak ada if/elif/else")
        
        word = []
        buffer = ""
        length = len(str)
        boolCheck = FA_boolean()
        for i in range(length):
            if (str[i] == " "):
                word.append(buffer)
                buffer = ""
            elif (str[i] == "(" or str[i] == ")"):
                word.append(buffer)
                word.append(str[i])
                buffer = ""
            else:
                buffer += str[i]
        if(buffer != ""):
            word.append(buffer)
        word = list(filter(lambda a: a!="", word))
        
        arr = ["if", "elif", "else",":","(",")"]
        for i in range(len(word)):
            if word[i] not in arr:
                try:
                    boolCheck.checkBoolStatement(word[i])     
                except Exception as e: 
                    raise e
                else:
                    word[i] = "VAR"