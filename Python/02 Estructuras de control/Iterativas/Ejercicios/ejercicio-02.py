numDolares = int(input("Para cuantos dolares? "))
precioDolar = float (input("Cotización del dolar: "))

for i in range (1, numDolares + 1) :
  pesos = i * precioDolar
  print ("%4d dolares equivalen a $ %8.2f" % (i, pesos))

