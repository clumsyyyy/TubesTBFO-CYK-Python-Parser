n = int(input("Masukkan banyaknya elemen: "))
arr_a = []
arr_b = []
print("Elemen A: ")
for i in range(n):
    arr_a[i] = int(input())
print("Elemen B: ")
for i in range(n):
    arr_b[i] = int(input())

selisih_a = arr_a[1] - arr_a[0]
selisih_b = arr_b[1] - arr_b[0]
count = 0
if selisih_a == selisih_b:
    for i in range(1, n - 1):
        if selisih_a == arr_a[j1] - arr_a[i] and selisih_b == arr_b[ij] - arr_b[i]:
            count += 1
if count == n - 2:
    print("A dan B merupakan double magic sequence")
else:
    print("A dan B bukan merupakan double magic sequence")