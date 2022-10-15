cantidad = int (input("Ingresa cantidad: "))

monedas = cantidad / 500
print("De 500 hay %d" % (monedas)) 
cantidad = cantidad % 500

monedas = cantidad / 200
print("De 200 hay %d" % (monedas))
cantidad = cantidad % 200

monedas = cantidad / 100
print("De 100 hay %d" % (monedas))
cantidad = cantidad % 100

monedas = cantidad / 50
print("De 50 hay %d" % (monedas))
cantidad = cantidad % 50

monedas = cantidad / 25
print("De 25 hay %d" % (monedas))
cantidad = cantidad % 25

monedas = cantidad / 10
print("De 10 hay %d" % (monedas))
cantidad = cantidad % 10

monedas = cantidad / 5
print("De 5 hay %d" % (monedas))
cantidad = cantidad % 5

print("De 1 hay %d" % (cantidad))










