

def dead_varname(str):
    if (str == ''):
        return False
    else:
        return dead_varname(str[1:])

def final_varname(str):
    if (str == ''):
        return True
    elif (str[0].isalpha() or str[0] == '_' or str[0].isdigit()):
        return final_varname(str[1:])
    else:
        return dead_varname(str[1:])

def start_varname(str):
    if (str == ''):
        return False
    elif (str[0].isalpha() or str[0] == '_'):
        return final_varname(str[1:])
    else:
        return dead_varname(str[1:])

def isValid_varname(str):
    return start_varname(str)

print(isValid_varname('2sadksadas'))