cadena="ATGCAAATTGTGTGTGCATAATTTATATAGGCTAGAATAGAATCGCTA"
pares = len(cadena)/2
cuenta = cadena.count("GC")

porcentaje = cuenta / pares * 100

print("%.4f %%" % (porcentaje)) 



