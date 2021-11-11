print("=====GEBYAR DISKON=====")
print("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")
ka = int(input("KIPAS ANGIN DISKON 10%      Rp 25.000,00 : "))
sd = int(input("SEPEDA DISKON 55%           Rp 6.000,00 : "))
hr = int(input("HELM ROSSI DISKON 77%       Rp 8.000,00 : "))

tka = (25000*10/100)*ka
tsd = (6000*55/100)*sd
thr = (8000*77/100)*hr

print("=====TOTAL=====")
print("TOTAL KIPAS ANGIN    : Rp ",tka)
print("TOTAL SEPEDA SUPER   : Rp ",tsd)
print("TOTAL HELM ROSSI     : Rp ",thr)
print("Jumlah total bayar yang harus dibayar adalah Rp ",tka+tsd+thr)




