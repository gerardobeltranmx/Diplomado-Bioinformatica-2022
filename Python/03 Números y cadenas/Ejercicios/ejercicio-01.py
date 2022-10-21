texto = input ("Escribe un texto: ")
texto = texto.upper()
a = texto.count("A")
e = texto.count("E")
i = texto.count("I")
o = texto.count("O")
u = texto.count("U")

total = a + e + i + o + u
print("Se encontraron %d vocales" % (total))

