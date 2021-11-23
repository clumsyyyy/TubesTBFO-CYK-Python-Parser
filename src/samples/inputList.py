def teeteedGwKecil():
    return 5 <= 6 & "a" in "yahoo

def list():
    N = int(input("Input N: "))
    stocks = []
    for i in range(N):
        stocks[i] = int(input("stonks today: "))
    profit = 0
    for i in range(N):
        for j in range(i, N):
            if stocks[j] - stocks[i] >= profit:
                profit = stocks[j] - stocks[i]
    if ((profit)>0) and (teeteedGwKecil()):
        print("stonks")
    else:
        print("not stonks")

