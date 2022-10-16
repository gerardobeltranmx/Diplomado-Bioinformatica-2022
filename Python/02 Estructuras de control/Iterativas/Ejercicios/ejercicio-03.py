inicio = int(input ("Centimetros iniciales: "))
fin = int(input ("Centimetros finales: "))

print ("%12s %8s %8s %8s" % ("centimetros", "metros", "yardas", "pulgadas"))
for cm in range(inicio, fin + 1) :
  metros = cm / 100
  yardas = cm / 91.44
  pulgadas = cm / 2.54
  print ("%12d %8.3f %8.3f %8.3f" % (cm, metros, yardas, pulgadas))

  