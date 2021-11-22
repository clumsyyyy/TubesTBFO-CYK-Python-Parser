# CYK-Python-Parser
> _Parser_ bahasa _Python_ menggunakan algoritma Cocke-Younger-Kasami dan CFG dalam bentuk CNF - Tugas Besar IF2124 Teori Bahasa Formal dan Otomata


## Informasi
Program ini adalah program yang mengecek _grammar_ dari suatu file `.py` dan memberikan _output_ apakah file tersebut valid untuk dikompilasi (program ini tidak bisa mengkompilasi, hanya menganalisis _grammar_). _Grammar_ dari bahasa _Python_ dibuat dalam bentuk _context-free language_ dan diubah ke bentuk _Chomsky normal form_ (CNF), yang kemudian dimasukkan ke algoritma _Cocke-Younger-Kasami_ (CYK) untuk mengecek _grammar_ dari input string per baris yang telah diproses.

_Pasrer_ ini dibuat menggunakan _interpreter Python 3.9.1_.

## Cara penggunaan
1. Jalankan file `main.py` (untuk sekarang `main_utils.py`)
2. Masukkan nama/direktori file berimbuhan `.py` yang ingin dicek (file juga dapat dimasukkan dalam format `.txt`
3. Program akan mengecek isi dari file `.py` secara baris per baris, dan mengeluarkan error apabila ada kesalahan dalam program

## Anggota
1. 13520124 - Owen Christian Wijaya
2. 13520152 - Muhammad Fahmi Irfan
3. 13520157 - Thirafi Najwan Kurniatama
