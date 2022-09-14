import time
problemSize = 1
print("%12s%16s%12s%16s" %("n^4", "segundos", "2n", "segundos"))

while True:
  start = time.time()
  work = 1
  for x in range(4):
    problemSize * problemSize
    elapsed1 = time.time() - start
  for x in range(1):
    problemSize + problemSize
    elapsed2 = time.time() - start
  print("%12s%16s%12s%16s" %("", elapsed1, "", elapsed2))
  problemSize += 1