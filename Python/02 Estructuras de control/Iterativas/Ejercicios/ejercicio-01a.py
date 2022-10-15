N = int(input("Cantidad de parejas de valores: "))
T = 0
for i in range(1, N + 1) :
  A = int (input("Valor A: "))
  B = int (input("Valor B: "))
  C = A + B
  T = T + C
  print (C)
  
print (T)  