number1 = 5
number2 = 10

# Operator Perbandingan 
if number1 != number2 :
    print("Nomor Berbeda")
else:
    print("Nomor Sama")

# Operator Logika
if number1 > 99 and number1 <1000:
    print("Bilangan Ratusan")
else:
    print("Bukan Bilangan Ratusan")

# Operator aritmatika
while True:
    number3 = int(input("Masukan Angka: "))
    
    if number3 == 00:
        break

    if number3 % 2 == 0:
        print("Bilangan Genap")
    else: 
        print("Bilangan Ganjil")