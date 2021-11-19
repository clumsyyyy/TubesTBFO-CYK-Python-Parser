import sys
<<<<<<< HEAD:src/utilities/LOOP_driver.py
sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")

from cykchecker import cykcheck 
=======
#sys.path.append("C:\\reverseon\\code\\github\\TubesTBFO\\src\\")
sys.path.append("C:\\Users\\OWEN\\OneDrive\\Documents\\IF Sem 3\\TBFO\\Tubes\\TubesTBFO\\src\\")
from cykchecker import cykcheck
>>>>>>> 569b0ca6db325d8a048db0f15dd5aee051a61bda:src/parser/loop/driver.py
from FA import FA_function
from CNF import CNF_functionargs

funVarCheck = FA_function.FA_VALIDFUNVARNAMEC()
argsRule =  CNF_functionargs.CNF_LOOP()
cykChecker = cykcheck.CYKCHECKCLASS()
extractfnargs = FA_function.SEMIFA_EXTRACT_FUNNAME_ARGS_PARENTHESES()
fa_helper = FA_function.FA_function_HELPER()

try:
<<<<<<< HEAD:src/utilities/LOOP_driver.py
    fa_helper.checkforloopstatement("           for                asdsad         in        R(sa asd):          ")
=======
    fa_helper.checkforloopstatement("for i in range(5, 6, 1):")
>>>>>>> 569b0ca6db325d8a048db0f15dd5aee051a61bda:src/parser/loop/driver.py
except Exception as e:
    print(e.args[0] + ":", e.args[1])
else:
    print("Success")