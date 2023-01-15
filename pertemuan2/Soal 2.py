# Menghitung rata-rata (average)

# input untuk mengatur banyaknya angka
x = int(input('Masukan banyaknya angka = '))

# Variabel untuk nilai 0 buat penjumlahan
total = 0

# For dengan parameter perulangan sebanyak variabel x, kemudian melakukan penjumlahan masing-masing inputan 
for h in range(x):
    w = int(input(' Masukan angka = '))
    total = float((total + w))

# Menampilkan hasil penjumlahan kemudian dibagi banyaknya jumlah bilangan 
print('Rata-rata =', total/x)