class Mahasiswa:

     def __init__(self, merk):
         self.__merk = merk
         
     def tampilkan_merk(self):
         print(f'Nama: {self.__merk}')
jip = Mahasiswa('Muh.Rifki Anhar - D0219011')
jip.tampilkan_merk()
