class CNF_Boolean:
    def getBoolRule(self):
        return[
            ("S", ["True"]),
            ("S", ["False"]),
            ("S", ["VAR"]),
            ("S", ["FUNCALL"]),
            ("S", ["COMPARISON"]),
            ("S", ["INT"]),
            ("S", ["H0", "S"]),
            ("S", ["H1", "S"]),
            ("S", ["H2", "S"]),
            ("H0", ["not"]),
            ("H1", ["S", "H3"]),
            ("H2", ["S", "H4"]),
            ("H3", ["and"]),
            ("H4", ["or"])
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
class CNF_IMPORT:
    def getImportRule(self):
        # from METHOD import VAR as VAR
        # from METHOD import VAR
        # import METHOD
        # import METHOD as VAR 
        # from VAR import VAR as VAR
        # from VAR import VAR
        # import VAR
        # import VAR as VAR
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

class CNF_Equals:
    #equalArr = ['=', '+=', '-=', '//=', '*=', '/=', '%=']
    def getEqualsRule(self):
        return [
            ("S", ["H0", "S2"]),
            ("S", ["H1", "S2"]),
            ("S1", ["VAR"]),
            ("EQ", ["="]),
            ("EQ", ["+="]),
            ("EQ", ["-="]),
            ("EQ", ["//="]),
            ("EQ", ['*=']),
            ("EQ", ["/="]),
            ("EQ", ["%="]),
            ("S2", ["VAR"]),
            ("S2", ["LIST"]),
            ("S2", ["ARITH"]),
            ("S2", ["FUNCALL"]),
            ("S2", ["ASSIGN"]),
            ("NOT", ["not"]),
            ("H0", ["H1", "NOT"]),
            ("H1", ["S1", "EQ"])
        ]

class CNF_CONDITIONAL:
    def getCondRule(self):
        return [
            ("S", ["H0", "THEN"]),
            ("S", ["H1", "THEN"]),
            ("S", ["ELSE", "THEN"]),
            ("IF", ["if"]),
            ("STATEMENT", ["STATEMENT"]),
            ("ELIF", ["elif"]),
            ("ELSE", ["else"]),
            ("THEN", [":"]),
            ("H0", ["IF", "STATEMENT"]),
            ("H1", ["ELIF", "STATEMENT"]),
        ]
'''
  S -> H0 S2
     | H1 S2
 S1 -> "VAR"
 EQ -> "="
 S2 -> "VAR"
     | "LIST"
     | "ARITH"
     | "FUNCALL"
NOT -> "not"
 H0 -> H1 NOT
 H1 -> S1 EQ
 '''
 
class CNF_MISC:
    # class, def, pass, raise, return
    def getDefClass(self):
        return [
            ("S",["FUNCTION","THEN"]),
            ("S",["CLASS","THEN"]),
            ("FUNC",["FUNNAME","ARGS"]),
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
        
'''
   S -> H1 H0
      | H2 H0
ARGS -> VAR
      | H3 ARGS
  H0 -> :
  H1 -> H4 ARGS
  H2 -> H5 H6
  H3 -> H7 H8
  H4 -> H9 H6
  H5 -> class
  H6 -> FUNCAL
  H7 -> VAR
  H8 -> ,
  H9 -> def

'''