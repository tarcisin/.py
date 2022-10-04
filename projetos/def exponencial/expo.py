def expo(base, iter):
  res = base * base
  loopEx = iter - 2

  if iter < 0:
    print("Expoente negativo, operação inválida!")
    return False
    
  elif iter == 0:
    res = 1

  elif iter == 1:
    res = base

  for i in range(loopEx):
    res *= base
  
  return res

exec = expo(2, 1)

print(exec)