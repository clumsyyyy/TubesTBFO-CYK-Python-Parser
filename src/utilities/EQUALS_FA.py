from ARITH_helper import arithHelper
from CNF_general import CNF_Equals
from CYKCHECKER_general import CYKCHECKCLASS
from LOOP_FA_function import FA_VALIDFUNVARNAMEC, FA_function_HELPER

class FA_equals:
    def checkEqual(self, str):
        if "=" not in str:
            raise Exception("where =")
        word = str.split("=")
        
        #cek sisi kiri harusnya variabel
        varCheck = FA_VALIDFUNVARNAMEC()
        try:
            varCheck.check(word[0])
        except Exception as e:
            raise e
        else:
            word[0] = "VAR"        

        #cek sisi kanan
