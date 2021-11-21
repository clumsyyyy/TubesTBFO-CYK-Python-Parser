import sys
import sys

#sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")
#sys.path.append("C:\\Users\\OWEN\\OneDrive\\Documents\\IF Sem 3\\TBFO\\Tubes\\TubesTBFO\\src\\")
sys.path.append("D:\\FAHMI\\KULIAH\\SEMESTER 3\\TEORI BAHASA FORMAL DAN AUTOMATA\\TOOBES\\TubesTBFO\\src")

from cykchecker import cykcheck
from CNF import CNF_conditional
from FA import FA_conditional

cykChecker = cykcheck.CYKCHECKCLASS()
ruleCondtional = CNF_conditional.CNF_CONDITIONAL().get()

try:
    print(cykChecker.check(ruleCondtional, "i (v) :")) # <- ganti isi string kalo mo tes
    #FAChecker.checkComparisonStatement("5 < 6")
except Exception as e:
    print(e)
else:
    print("Nice")