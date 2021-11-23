a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))

if str(a/2) == "1.0": #jika koefisien a dibagi 2 sama dengan 1, maka print x^2 tanpa 1
    if b != 0:
        print("Integral dari f(x) adalah x^2 + " + str(b) + "x + C")
    elif b == 0:
        print("Integral dari f(x) adalah x^2 + C")
    elif b == 1:
        print("Integral dari f(x) adalah x^2 + x + C")
    elif b == -1:
        print("Integral dari f(x) adalah x^2 - x + C")
elif str(a/2) == "-1.0": #jika koefisien a dibagi 2 sama dengan -1, maka print -x^2 tanpa 1
    if b != 0:
        print("Integral dari f(x) adalah -x^2 + " + str(b) + "x + C")
    elif b == 0:
        print("Integral dari f(x) adalah -x^2 + C")
    elif b == 1:
        print("Integral dari f(x) adalah -x^2 + x + C")
    elif b == -1:
        print("Integral dari f(x) adalah -x^2 - x + C")
elif a == 0:
    print("Integral dari f(x) adalah " + str(b) + "x + C")
else:
    if (a / 2) % 1 == 0:#jika koefisien a dibagi 2 adalah bilangan bulat, maka print dengan tipe tidak berkoma
        if b != 0:
            print("Integral dari f(x) adalah " + str(int(a / 2)) + "x^2 + " + str(b) + "x + C")
        elif b == 0:
            print("Integral dari f(x) adalah " + str(int(a / 2)) + "x^2 +  C")
    elif (a / 2) % 1 != 0:#jika koefisien a dibagi 2 bukan bilangan bulat, maka print dengan tipe berkoma
        if b != 0:
            print("Integral dari f(x) adalah " + str(a / 2) + "x^2 + " + str(b) + "x + C")
        elif b == 0:
            print("Integral dari f(x) adalah " + str(a / 2) + "x^2 +  C")