num = int(input("¿Qué tabla quieres mostrar?  "))
for i in range(1, 11):
  valor = num * i
  print("%5d x %8d = %10d" % (i,  num, valor))
