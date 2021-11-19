class CNF_Boolean:
    def get(self):
        return [
            ("S", ["H0", "S2"]),
            ("S1", ["True", "False"]),
            ("S2", ["True", "False"]),
            ("Op", ["and", "or"]),
            ("w", ["H1", "H1"]),
            ("Not", ["not", ""])
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