temp = int(input("Indica temperatura: "))

if temp < 0 :
  print("Muy Frio")
elif temp >= 0 and temp <= 10 :
  print ("Frio")
elif temp>10 and temp <= 20 :
  print("Templado")
elif temp > 20 and temp <= 25 :
  print ("Calido")
else :
  print ("Muy calido")