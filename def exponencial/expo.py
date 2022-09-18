def expo(base, iter):
  res = base * base
  loopEx = iter - 2

  if iter < 0:
    print("Expoente negativo, operação inválida!")
    return False
  for i in range(loopEx):
    res *= base
  
  return res

exec = expo(27, 4)

print(exec)