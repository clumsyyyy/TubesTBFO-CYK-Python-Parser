import CNF_general as CNFINST
import CYKCHECKER_general as CYKCHECK
import LOOP_FA_function as LOOP_FA

faInst = CNFINST.CNF_IMPORT()
funvarChecker = LOOP_FA.FA_VALIDFUNVARNAMEC()

def checkimp(str):
    str = str.rstrip()
    word = str.split()
    print(word)

checkimp("      from ggimport gaming             ")