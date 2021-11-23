# CYK-Python-Parser
> _Parser_ bahasa _Python_ menggunakan algoritma Cocke-Younger-Kasami dan Chomsky Normal Form
> Tugas Besar IF2124 Teori Bahasa Formal dan Otomata


## Informasi
Program ini adalah program yang mengecek _grammar_ dari suatu file `.py` dan memberikan _output_ apakah file tersebut valid untuk dikompilasi (program ini tidak bisa mengkompilasi, hanya menganalisis _grammar_). _Grammar_ dari bahasa _Python_ dibuat dalam bentuk _context-free language_ dan diubah ke bentuk _Chomsky normal form_ (CNF), yang kemudian dimasukkan ke algoritma _Cocke-Younger-Kasami_ (CYK) untuk mengecek _grammar_ dari input string per baris yang telah diproses.

_Parser_ ini dibuat menggunakan _interpreter Python 3.9.1_.


## Cara Penggunaan
1. Pastikan eksekusi dilakukan di dalam folder `src`
2. Buka terminal, gunakan perintah:`py main.py <nama-file>.py` (misal. `py main.py inputAcc.py`)
    * **[IMPORTANT]** pastikan file yang ingin dicek ada di dalam folder `samples`
    * File bertipe _plaintext_ (`.txt`) juga bisa diuji
3. Program akan membaca isi dari file secara baris per baris
    * Apabila file benar, maka program akan memberikan _output_ validasi
    * Apabila ada kesalahan, program akan berhenti dan memberikan _output_ baris yang salah

## Fitur Tambahan
1. _Output_ letak baris kesalahan sintaks program (apabila terdapat kesalahan)
2. Algoritma rekursif untuk _parsing_ struktur data (_list, boolean, comparison statement_)
3. _Parser_ sintaks yang modular sehingga dapat diinspeksi terpisah
4. Validasi struktur data dan persamaan _assignment_
5. Validasi indentasi untuk kondisional dan perulangan
6. Validasi kata kunci perulangan (`break`, `continue`, `pass`)

## Anggota
1. 13520124 - Owen Christian Wijaya
2. 13520152 - Muhammad Fahmi Irfan
3. 13520157 - Thirafi Najwan Kurniatama
