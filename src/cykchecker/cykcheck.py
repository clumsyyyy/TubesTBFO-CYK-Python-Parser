from itertools import product as cp
import itertools

class CYKCHECKCLASS:
    def tuple_to_arr(self, tuple):
        return list(tuple)

    def checkrulethatproduces(self, rule, word):
        availrule = []
        for (x,y) in rule:
            if y == word:
                availrule.append(x)
        return availrule

    def check(self, rule, word) -> bool:
        tablesize = len(word)
        cyktable = [[None for i in range(tablesize)] for j in range(tablesize)]
        for stage in range(tablesize):
            for diag in range(0, tablesize - stage):
                # cyktable[diag][diag + stage]
                if stage == 0:
                    cyktable[diag][diag + stage] = self.checkrulethatproduces(rule, [word[diag]])
                else:
                    totalrule = []
                    i = diag
                    j = diag + stage
                    for jcell in range(diag, j):
                        if cyktable[i][jcell] == None or cyktable[jcell + 1][j] == None:
                            continue
                        else:
                            productcombin = [item for item in cp(cyktable[i][jcell], cyktable[jcell+1][j])]
                            tosearchrule = map(self.tuple_to_arr, productcombin)
                            for wordsearch in tosearchrule:
                                availrule = self.checkrulethatproduces(rule, wordsearch)
                                totalrule = totalrule + availrule
                    totalrule = list(set(totalrule)) # REMOVE DUPLICATES
                    if (len(totalrule) == 0):
                        cyktable[i][j] = None
                    else:
                        cyktable[i][j] = totalrule
        if (cyktable[0][tablesize - 1] == None):
            return False
        else:
            (startrule, _)= rule[0]
            if (startrule in cyktable[0][tablesize - 1]):
                return True
            else:
                return False


initInst = CYKCHECKCLASS()

rule = [
    ("S", ["A", "B"]),
    ("S", ["B", "C"]),
    ("GAMING", ["AD", "A"]),
    ("A", ["B", "A"]),
    ("A", ["a"]),
    ("B", ["CB", "C"]),
    ("AD", ["ManTAP"]),
    ("DA", ["LB", "A"]),
    ("B", ["b"]),
    ("C", ["A", "B"]),
    ("C", ["a"]),
    ("CB", ["cb"]),
    ("LB", ["cb"]),
]
