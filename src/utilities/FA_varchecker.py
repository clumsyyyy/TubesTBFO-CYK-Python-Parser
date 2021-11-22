class varNameChecker:
    def __init__(self):
        self.res = True

    def _start(self, str) -> bool:
        self.res = True
        if (str == ''):
            self._dead('')
        elif (str[0] == '_' or str[0].isalpha()):
            self._finish(str[1:])
        else:
            self._dead(str[1:])
        return self.res
        
    def _finish(self, str):
        if (str == ''):
            self.res = True
        elif (str[0] == '_' or str[0].isalpha() or str[0].isdigit()):
            self._finish(str[1:])
        else:
            self._dead(str[1:])

    def _dead(self, str):
            raise Exception(["Invalid variable/function name"])
            self.res = False
            
    def check(self, str):
        return self._start(str)