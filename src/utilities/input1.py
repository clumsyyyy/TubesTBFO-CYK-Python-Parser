from BOOL_FA import FA_equals as FAe

def makloGaming(count):
    for i in range(1, 10, 3):
        if count % 2 == 0:
            count += 1
        else:
            count -= 2
    while count <= 128:
        count //= 2
    return count