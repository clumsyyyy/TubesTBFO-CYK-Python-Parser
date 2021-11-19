import sys
sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")

from CNF import CNF_import
from parser.loop.FA import FA_function

faInst = CNF_import.CNF_IMPORT()
funvarChecker = FA_function.FA_VALIDFUNVARNAMEC()

def checkimp(str):
    str = str.rstrip()
    word = str.split()
    print(word)

checkimp("      from gg import gaming             ")