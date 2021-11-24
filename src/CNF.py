class CNF_Boolean:
    def getBoolRule(self):
        return [
            ("START", ["H0", "INST"]),
            ("START", ["H1", "TWO"]),
            ("START", ["INT"]),
            ("START", ["VAR"]),
            ("START", ["BOOLOPS"]),
            ("START", ["STR"]),
            ("START", ["LIST"]),
            ("START", ["FUNCALL"]),
            ("START", ["COMP"]),
            ("START", ["H2", "INST"]),
            ("START", ["False"]),
            ("START", ["True"]),
            ("START", ["None"]),
            ("TWO", ["H3", "TWO"]),
            ("TWO", ["BOOLOPS"]),
            ("TWO", ["STR"]),
            ("TWO", ["LIST"]),
            ("TWO", ["FUNCALL"]),
            ("TWO", ["VAR"]),
            ("INST", ["INT"]),
            ("INST", ["VAR"]),
            ("INST", ["BOOLOPS"]),
            ("INST", ["STR"]),
            ("INST", ["LIST"]),
            ("INST", ["FUNCALL"]),
            ("INST", ["COMP"]),
            ("INST", ["False"]),
            ("INST", ["True"]),
            ("INST", ["None"]),
            ("INST", ["H0", "INST"]),
            ("INST", ["H2", "INST"]),
            ("NIINST", ["BOOLOPS"]),
            ("NIINST", ["STR"]),
            ("NIINST", ["LIST"]),
            ("NIINST", ["FUNCALL"]),
            ("NIINST", ["VAR"]),
            ("NIINST", ["False"]),
            ("NIINST", ["True"]),
            ("NIINST", ["None"]),
            ("NI", ["not in"]),
            ("NI", ["in"]),
            ("BIN", ["and"]),
            ("BIN", ["or"]),
            ("H0", ["INST", "BIN"]),
            ("H1", ["INST", "NI"]),
            ("H2", ["not"]),
            ("H3", ["NIINST", "NI"])
        ]
    def getIsRule(self):
        return [
            ("S", ["H0", "S2"]),
            ("S", ["H1", "S2"]),
            ("S", ["H2", "S2"]),
            ("S", ["H3", "S2"]),
            ("S1", ["VAR"]),
            ("S2", ["VAR"]),
            ("IS", ["is"]),
            ("Not", ["not"]),
            ("H0", ["H2", "Not"]),
            ("H1", ["H3", "Not"]),
            ("H2", ["H4", "IS"]),
            ("H3", ["S1", "IS"]),
            ("H4", ["Not", "S1"])
        ]
    def getNewIsRule(self):
        return [
            ("S", ["H0", "S"]),
            ("S", ["NOT", "S1"]),

        ]
class CNF_IMPORT:
    def getImportRule(self):
        return [
            ("START", ["H1", "H0"]),
            ("START", ["H2", "H0"]),
            ("START", ["H3", "MV"]),
            ("START", ["H4", "H0"]),
            ("MV", ["METHOD"]),
            ("MV", ["VAR"]),
            ("H0", ["VAR"]),
            ("H1", ["H5", "H3"]),
            ("H2", ["H7", "H6"]),
            ("H3", ["import"]),
            ("H4", ["H8", "H6"]),
            ("H5", ["H9", "MV"]),
            ("H6", ["as"]),
            ("H7", ["H1", "H0"]),
            ("H8", ["H3", "MV"]),
            ("H9", ["from"])
        ]
    def getMethodRule(self):
        # VAR. ... VAR
        return [
            ("START", ["H0", "B"]),
            ("B", ["H0", "B"]),
            ("B", ["VAR"]),
            ("H0", ["H1", "H2"]),
            ("H1", ["VAR"]),
            ("H2", ["."])
        ]

class CNF_LOOP:
    

    def getListElRule(self):
        return [
            ("START", ["H0", "EC"]),
            ("EC", ["H1", "EC"]),
            ("EC", ["H3", "H2"]),
            ("CALEE", ["VAR"]),
            ("CALEE", ["NUM"]),
            ("CALEE", ["BOOL"]),
            ("CALEE", ["FUNCALL"]),
            ("CALEE", ["ARITH"]),
            ("H0", ["VAR"]),
            ("H1", ["H3", "H2"]),
            ("H2", ["]"]),
            ("H3", ["H4", "CALEE"]),
            ("H4", ["["]),
        ]
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
            ("O", ["LIST"]),
            ("O", ["STR"]),
            ("O", ["BOOLOPS"]),
            ("O", ["INT"]),
            ("O", ["COMP"]),
            ("O", ["ARITH"]),
            ("O", ["FLOAT"]),
            ("H0", [":"]),
            ("H1", ["H2", "O"]),
            ("H2", ["H4", "H3"]),
            ("H3", ["in"]),
            ("H4", ["H5", "H6"]),
            ("H5", ["for"]),
            ("H6", ["VAR"]),
        ]
    def getWhileLoopRule(self):
        return [
            ("START", ["H1", "H0"]),
            ("H1", ["H4", "TYP"]),
            ("TYP", ["VAR"]),
            ("TYP", ["FUNCALL"]),
            ("TYP", ["BOOL"]),
            ("H4", ["while"]),
            ("H0", [":"]),
        ]
    def getWithRule(self):
        return [
            ("START", ["H1", "H0"]),
            ("FINST", ["VAR"]),
            ("FINST", ["FUNCALL"]),
            ("H0", [":"]),
            ("H1", ["H3", "H2"]),
            ("H2", ["VAR"]),
            ("H3", ["H5", "H4"]),
            ("H4", ["as"]),
            ("H5", ["H6", "FINST"]),
            ("H6", ["with"]),
        ]

class CNF_Equals:
    def getEqualsRule(self):
        return [
            ("S", ["H0", "S2"]),
            ("S", ["H1", "S2"]),
            ("S", ["H2", "S3"]),
            ("S", ["H3", "S2"]),
            ("S1", ["VAR"]),
            ("S1", ["LISTEL"]),
            ("EQ", ["="]),
            ("EQ2", ["+="]),
            ("EQ2", ["-="]),
            ("EQ3", ['*=']),
            ("EQ3", ['**=']),
            ("EQ3", ["/="]),
            ("EQ3", ["//="]),
            ("EQ3", ["**="]),
            ("EQ3", [":="]),
            ("EQ3", ["@="]),
            ("EQ3", ["%="]),
            ("S2", ["VAR"]),
            ("S2", ["LIST"]),
            ("S2", ["ARITH"]),
            ("S2", ["FUNCALL"]),
            ("S2", ["BOOL"]),
            ("S2", ["ASSIGN"]),
            ("S2", ["INT"]),
            ("S3", ["VAR"]),
            ("S3", ["ARITH"]),
            ("S3", ["FUNCALL"]),
            ("S3", ["INT"]),
            ("NOT", ["not"]),
            ("H0", ["H3", "NOT"]),
            ("H1", ["S1", "EQ2"]),
            ("H2", ["S1", "EQ3"]),
            ("H3", ["S1", "EQ"])
        ]

class CNF_CONDITIONAL:
    def getCondRule(self):
        return [
            ("S", ["H0", "THEN"]),
            ("S", ["H1", "THEN"]),
            ("S", ["H2", "THEN"]),
            ("S", ["ELSE", "THEN"]),
            ("IF", ["if"]),
            ("WHILE", ["while"]),
            ("STATEMENT", ["STATEMENT"]),
            ("ELIF", ["elif"]),
            ("ELSE", ["else"]),
            ("THEN", [":"]),
            ("H0", ["IF", "STATEMENT"]),
            ("H1", ["ELIF", "STATEMENT"]),
            ("H2", ["WHILE", "STATEMENT"])
        ]
 
class CNF_Freetype:
    # class, def, pass, raise, return
    def getDefClass(self):
        return [
            ("S",["FUNCTION","THEN"]),
            ("S",["CLASS","THEN"]),
            ("FUNC",["FUNNAME","ARGS"]),
            ("FUNC", ["FUNNAME"]),
            ("ARGS",["VAR"]),
            ("ARGS",["VAR","ARGS"]),
            ("VAR",["VAR"]),
            ("CLASSNAME",["FUNNAME"]),
            ("CLASSNAME",["FUNNAME","ARGS"]),
            ("FUNNAME",["FUNNAME"]),
            ("THEN",[":"]),
            ("FUNCTION",["DEF","FUNC"]),
            ("CLASS",["CLASSKEYWORD","CLASSNAME"]),
            ("CLASSKEYWORD",["class"]),
            ("DEF",["def"]),
        ]
    
    def getPassReturnRaise(self):
        return [
            ("S", ["return"]),
            ("S",["pass"]),
            ("S",["RETURN","STATEMENT"]),
            ("S",["RAISE","EXCEPTION"]),
            ("STATEMENT", ["STATEMENT"]),
            ("STATEMENT", ["INT"]),
            ("STATEMENT", ["STRING"]),
            ("STATEMENT", ["LIST"]),
            ("STATEMENT", ["VAR"]),
            ("RETURN",["return"]),
            ("RAISE",["raise"]),
            ("EXCEPTION",["EXCEPTION"])
        ]
    
