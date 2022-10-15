peso = float(input("Indicar el peso: "))
estatura = float(input("Indicar la estatura: "))

IMC = peso / estatura**2

print("%.4f" % (IMC))

if (IMC < 25):
  print ("NORMAL")
else:
  print ("SOBREPESO") 
