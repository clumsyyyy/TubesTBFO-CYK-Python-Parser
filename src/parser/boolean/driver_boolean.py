import sys

#sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")
sys.path.append("C:\\Users\\OWEN\\OneDrive\\Documents\\IF Sem 3\\TBFO\\Tubes\\TubesTBFO\\src\\")
from CNF import CNF_boolean
from FA import FA_boolean
FAChecker = FA_boolean.FA_boolean()

try:
    FAChecker.checkBoolStatement("((not(5)) and (not(7)))") # <- ganti isi string kalo mo tes
    #FAChecker.checkComparisonStatement("5 < 6")
except Exception as e:
    print(e)
else:
    print("Nice")