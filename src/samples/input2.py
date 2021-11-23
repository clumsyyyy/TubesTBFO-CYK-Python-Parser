#Algoritma:
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))
max = 0#Kemungkinan range adalah nilai terbesar, karena nilai terbesar bisa saja menjadi FPB
if d >= c and d <= b and d >= a: #jika d lebih besar dari nilai lain
    max = d
elif a >= b and a >= c and a >= d: #jika a lebih besar dari nilai lain
    max = a
elif c >= a and c >= b and c >= d: #jika c lebih besar dari nilai lain
    max = c
elif b >= a and b >= c and b >= d:
    max = b #jika b lebih besar dari nilai lain

ans = 0
for i in range(1, max + 1):
    if a % i == 0 and b % i == 0 and c % i == 0 and d % i == 0: #jika ditemukan i yang habis membagi keempat bilangan, i adalah FPB
        ans = i
print("FPB dari keempat bilangan tersebut adalah ", ans)