PI = 3.141592
# Entrada 
r = float(input("Indica el radio: "))
h = float(input("Indica el altura: "))
# Pricesos
At = 2 * PI * r * h + 2 * PI * r**2
Vt = PI * r**2 * h
# Salida
print ("AREA=%.2f" % At)
print ("VOLUMEN=%.2f" % Vt)



