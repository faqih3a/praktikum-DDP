# Mencetak persegi

# input untuk banyaknya sisi persegi
x = int(input('Masukan sebuah bilangan bulat = '))

print() #print untuk menambah baris baru seperi <br>

# For pertama untuk membuat perulangan secara vertikal
for h in range(x):

    # For kedua untuk membuat perulangan secara horizontal
    for w4 in range(x):

        # Print ' #' untuk mengatur karakter dan menampilkan perulangan secara horizontal, end untuk mengatur akhiran supaya berbentuk persegi 
        print(' #',end='')

    print() # Untuk menampilkan perulangan secara vertikal

print() # Print untuk menambah baris baru seperi <br>