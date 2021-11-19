class CNF_Boolean:
    def getBooleanRule(self):
        return [
            ("S", ["H0", "S2"]),
            ("S", ["H1", "S2"]),
            ("S", ["H2", "S2"]),
            ("S", ["H3", "S2"]),
            ("S1", ["True"]),
            ("S1", ["False"]),
            ("S2", ["True"]),
            ("S2", ["False"]),
            ("Not", ["not"]),
            ("Op", ["and"]),
            ("Op", ["or"]),
            ("H0", ["H2", "Not"]),
            ("H1", ["H3", "Not"]),
            ("H2", ["H4", "Op"]),
            ("H3", ["S1", "Op"]),
            ("H4", ["Not", "S1"])
        ]

class CNF_IMPORT:
    def getImportRule(self):
        return [
            ("START", ["H1", "H0"]),
            ("START", ["H2", "H0"]),
            ("START", ["H3", "H0"]),
            ("H0", ["VAR"]),
            ("H1", ["H5", "H4"]),
            ("H2", ["H6", "H3"]),
            ("H3", ["import"]),
            ("H4", ["as"]),
            ("H5", ["H2", "H0"]),
            ("H6", ["H7", "H0"]),
            ("H7", ["from"])
        ]



class CNF_LOOP:
    def getArgsRule(self):
        return [
        ("S", ["H0", "S"]),
        ("S", ["V"]),
        ("H0", ["H1", "H2"]),
        ("H1", ["V"]),
        ("H2", [","]),
        ]
    def getForLoopRule(self):
        return [
            ("START", ["H1", "H0"]),
            ("O", ["VAR"]),
            ("O", ["FUNCALL"]),
            ("H0", [":"]),
            ("H1", ["H2", "O"]),
            ("H2", ["H4", "H3"]),
            ("H3", ["in"]),
            ("H4", ["H5", "H6"]),
            ("H5", ["for"]),
            ("H6", ["VAR"]),
        ]