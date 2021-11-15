from itertools import product as cp

def join_tuple_string(strings_tuple) -> str:
   return ''.join(strings_tuple)

def checkrulethatproduces(rule, word):
    availrule = []
    for (x,y) in rule:
        if y == word:
            availrule.append(x)
    return availrule

def checkcyk(rule, str):
    tablesize = len(str)
    cyktable = [[None for i in range(tablesize)] for j in range(tablesize)]
    for stage in range(tablesize):
        for diag in range(0, tablesize - stage):
            # cyktable[diag][diag + stage]
            if stage == 0:
                cyktable[diag][diag + stage] = checkrulethatproduces(rule, str[diag])
            else:
                totalrule = []
                i = diag
                j = diag + stage
                for jcell in range(diag, j):
                    if cyktable[i][jcell] == None or cyktable[jcell + 1][j] == None:
                        continue
                    else:
                        productcombin = [item for item in cp(cyktable[i][jcell], cyktable[jcell+1][j])]
                        tosearchrule = map(join_tuple_string, productcombin)
                        for wordsearch in tosearchrule:
                            availrule = checkrulethatproduces(rule, wordsearch)
                            totalrule = totalrule + availrule
                totalrule = list(set(totalrule))
                if (len(totalrule) == 0):
                    cyktable[i][j] = None
                else:
                    cyktable[i][j] = totalrule
    return cyktable



rule = [
    ("S", "AB"),
    ("S", "BC"),
    ("A", "BA"),
    ("A", "a"),
    ("B", "CC"),
    ("B", "b"),
    ("C", "AB"),
    ("C", "a"), # SECTION INI UNTUK CEK VARIABLE
]

"""
 S -> H0 T
 V -> return
 T -> None
    | False
    | True
 W -> w
H0 -> V W
"""

rulereturn = [
    ("S", "ZT"),
    ("V", "return"),
    ("T", "VALIDRTYPE"),
    ("W", " "),
    ("Z", "VW")
]

str = ["return", " ", "INVALIDRTYPE"]

if (str[2] == 'None' or str[2] == 'False' or str[2] == 'True'): # or isValid_varname(str[2])
    str[2] = 'VALIDRTYPE'
else:
    str[2] = 'INVALIDRTYPE'
strlen = len(str)
print(checkcyk(rulereturn, str)[0][strlen-1])
