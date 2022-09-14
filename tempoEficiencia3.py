import time
problemSize = int(input("Insira o valor base do problema: "))
print("%12s%16s" %("ProblemSize", "Seconds"))
c = 0
while problemSize > 0:
  elapsed = 0
  problemSize = problemSize // 2
  c+=1
  problemSize*= 2

print("%12d%16.3f" % (c))
