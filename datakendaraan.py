class kendaraan:
   def __init__(self, inputnama_kendaraan, inputmerek): 
       self.nama_kendaraan = inputnama_kendaraan
       self.merek = inputmerek
kendaraan1 = kendaraan("motor", "Honda Beat")
kendaraan2 = kendaraan("mobil", "Toyota")

print(kendaraan1.__dict__)
