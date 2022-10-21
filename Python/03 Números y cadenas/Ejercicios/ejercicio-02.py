texto = input ("Escribe un texto: ")
texto = texto.upper()
a = texto.count("A")
e = texto.count("E")
i = texto.count("I")
o = texto.count("O")
u = texto.count("U")
espacios = texto.count(" ")
totalVocales = a + e + i + o + u
longitud = len(texto)
consonantes = longitud - espacios - totalVocales

print("Se encontraron %d consonantes" % (consonantes))
print("Se encontraron %d vocales A" % (a))
print("Se encontraron %d vocales E" % (e))
print("Se encontraron %d vocales I" % (i))
print("Se encontraron %d vocales O" % (o))
print("Se encontraron %d vocales U" % (u))



