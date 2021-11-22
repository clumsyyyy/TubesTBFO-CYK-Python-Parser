import CNF_general as CNFINST
import CYKCHECKER_general as CYKCHECK
import LOOP_FA_function as LOOP_FA

faInst = CNFINST.CNF_IMPORT()
funvarChecker = LOOP_FA.FA_VALIDFUNVARNAMEC()

def checkmethod(str):
    trig = False
    LatestCatch = ""
    str = str.strip()
    tword = str.split('.')
    # word = (' '.join(str.split())).split()
    word = []
    twlen = len(tword)
    for i in range(twlen):
        word = word + (' '.join(tword[i].split())).split()
        if (i != twlen - 1):
            word.append(".")
    wlen = len(word)
    print(word)
    for i in range(wlen):
        if (i % 2 == 0):
            try:
                funvarChecker.check(word[i])
            except Exception as e:
                trig = True
                LatestCatch = e
                word[i] = "INVALID"
            else:
                word[i] = "VAR"
    print(word)
    cykCheck = CYKCHECK.CYKCHECKCLASS()
    RuleInst = CNFINST.CNF_IMPORT()
    res = cykCheck.check(RuleInst.getMethodRule(), word)
    if (res):
        return True
    else:
        if (trig):
            raise Exception(["Invalid Method Statement"] + list(LatestCatch.args)[0])
            return
        else:
            raise Exception(["Invalid Method Statement"])
            

def checkimp(str):
    LatestCatch = ""
    trig = False
    str = str.rstrip()
    word = str.split(' ')
    word = [word[0]] + list(filter(lambda a: a != '', word[1:]))
    if (len(word) < 2):
        raise Exception(["Invalid Import Statement"])
        return
    wlen = len(word)
    caught = -1
    for i in range(1, wlen):
        if (word[i] == "import" or word[i] == "as"):
            caught = i
            break
    if (caught == -1):
        if (word[0] == "import"):
            caught = wlen
        else:
            raise Exception(["Invalid Import Statement"])
            return
    word[1] = ' '.join(word[1:caught])
    del word[2:caught]
    print("this", word)
    cykCheck = CYKCHECK.CYKCHECKCLASS()
    RuleInst = CNFINST.CNF_IMPORT()
    if (word[0] == ""):
        word[0] = " "
    wlen = len(word)
    for i in range(wlen):
        if i % 2 == 1:
            try:
                funvarChecker.check(word[i])
            except Exception as e:
                if (i == 1):
                    try:
                        checkmethod(word[i])
                    except Exception as e:
                        trig = True
                        LatestCatch = e
                        word[i] = "INVALID"
                    else:
                        word[i] = "METHOD"
                else:
                    trig = True
                    word[i] = "INVALID"
                    LatestCatch = e
            else:
                word[i] = "VAR"
    print(word)
    res = cykCheck.check(RuleInst.getImportRule(), word)
    if (res):
        return True
    else:
        if (trig):
            raise Exception(["Invalid Import Statement"] + list(LatestCatch.args)[0])
            return
        else:
            raise Exception(["Invalid Import Statement"])
# try:
#     checkimp("from a import b as c")
# except Exception as e:
#     print(e)
# else:
#     print("Success")