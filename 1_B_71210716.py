nl = input("Nama : ")
tampil = nl.split()

tampil.reverse()


ttl = str(input("Tempat tanggal lahir : "))
show = ttl.split()
tempat = show[0]
tl = show[1],show[2],show[3]


if len(tampil) < 3 :
  print("Haloo!", tampil[0] + ",", *tampil[1:])
else :
  print("Haloo!", tampil[0] + ",", *tampil[:-3:-1])
print("Anda Lahir di", tempat,"pada tanggal",*tl)