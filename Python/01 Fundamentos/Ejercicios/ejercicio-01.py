gradosCelsius = int(input("Escribe la temperatura en Celsius: "))
# gradosCelsius = int(gradosCelsius)
gradosFahrenheit = (gradosCelsius * 1.8) + 32
gradosKelvin = 273.15 + gradosCelsius
gradosRankine = (gradosCelsius * 1.8) + 491.67 

print ("%d" % (gradosFahrenheit))
print ("%.2f" % (gradosKelvin))
print ("%.2f" % (gradosRankine))
