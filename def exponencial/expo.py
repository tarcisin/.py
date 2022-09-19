def expo(base, iter):
  res = base * base
  loopEx = iter - 2

  if iter < 0:
    print("Expoente negativo, operação inválida!")
    return False
    
  elif iter == 0:
    res = 1

  for i in range(loopEx):
    res *= base
  
  return res

exec = expo(2, 16)

print(exec)