from ARITH_helper import arithHelper

inst = arithHelper()
try:
    inst.checkArithStatement("(2.22)") #mengontol variabel misalnya
except Exception as e:
    print(e)
else:
    print("Success")

"""
1. ada operator
2. cek ada operator yang salah tempat (*69)
3. cek jumlah kurung, sesuai atoga
4. cek jumlah operator yang ada
5. cek banyaknya operand (sekalian validasi variabel)
6. kalo jumlah operator >= jumlah operand, salah
7. kaloga bener
"""