peso = float(input("Indicar el peso: "))
estatura = float(input("Indicar la estatura: "))

IMC = peso / estatura**2

if (IMC < 25):
  print ("NORMAL")
else:
  print ("SOBREPESO") 
