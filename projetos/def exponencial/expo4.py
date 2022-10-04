def expo(number, exponent):
  if exponent == 0:
    number = 1

  elif (exponent % 2) == 0:
    number = (expo(number, exponent / 2)) * (expo(number, exponent / 2))
  
  elif (exponent % 2) != 0:
    number = number * expo(number, exponent - 1)

  return number

# A COMPLEXIDADE DESTE ALGORTIMO RECURSIVO É DE O(log N)