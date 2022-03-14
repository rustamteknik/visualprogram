print ("Rustam_D0219378")
def tambah(x, y):
   return x + y
def kurang(x, y):
   return x - y
def kali(x, y):
   return x * y
def bagi(x, y):
   return x / y
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

choice = input("silahkan pilih(1/2/3/4): ")
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(bil1,"+",bil2,"=", tambah(bil1,bil2))
elif choice == '2':
   print(bil1,"-",bil2,"=", kurang(bil1,bil2))
elif choice == '3':
   print(bil1,"*",bil2,"=", kali(bil1,bil2))
elif choice == '4':
   print(bil1,"/",bil2,"=", bagi(bil1,bil2))
else:
   print("Input salah")