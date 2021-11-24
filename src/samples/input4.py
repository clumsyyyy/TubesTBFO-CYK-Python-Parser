x = int(input("Masukkan X: "))

if x > 0:
    if x % 2 == 0:
        print("X adalah bilangan positif genap")
    elif x % 2 != 0:
        print("X adalah bilangan positif ganjil")

elif x < 0:
    print("X adalah bilangan negatif")
elif x == 0:
    print("X adalah bilangan nol")

