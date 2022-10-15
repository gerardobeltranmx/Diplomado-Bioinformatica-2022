N = int(input("Cantidad de parejas de valores: "))
T = 0
for i in range(1, N + 1) :
  A, B = input("Valor A y B: ").split(" ")
  #A = int(A)
  #B = int(B)
  C = int(A) +  int(B)
  T = T + C
  print (C)

print ("la suma total es %d " %  (T) )  