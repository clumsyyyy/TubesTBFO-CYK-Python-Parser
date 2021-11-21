import os
from CONDITIONAL_FA import FA_conditional

# path = input("Masukkan nama file...\n>>> ")

# while (not os.path.exists(path)):
#     print("File '", path, "' tidak ada!\n")
#     path = input("Masukkan nama file...\n>>> ")

# print("Membuka file", path, "...")

#dump instance
conditionals = FA_conditional()

#flags
ifFlag = False

#open file

count = 0
file = open("sampleInput.txt", "r", encoding="utf8")
for line in file:
    print("Line", count, ": ", end = "")
    expression = line.strip('\n')
    print(expression)
    try:
        conditionals.checkConditionals(expression)
    except Exception as e:
        print(e)
    else:
        print("Nice")
    # # evaluasi tiap line
    print("\n")
    count += 1
file.close()