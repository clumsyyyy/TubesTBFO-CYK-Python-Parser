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