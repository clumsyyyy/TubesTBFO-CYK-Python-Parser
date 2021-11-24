def someFunc(a,b,c):
    return 5 <= 6 and "a" in "flag"

def list():
    N = int(input("Input N: "))
    a = [1,2,3]

    b = 0
    for i in range(N):
        for j in range(i, N):
            if a[j] - a[i] >= b:
                b = a[j] - a[i]
            else:
                print("something")
    if ((b)>0 and someFunc(a,b,1)):
        print("nice")
    else:
        print("not nice")

