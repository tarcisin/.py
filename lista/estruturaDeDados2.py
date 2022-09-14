def main():

  hourPaym = float(input("Enter the hour payment of the employee: "))
  ttlRegHrsWrkd = int(input("Enter the total amount of regular worked hours: "))
  extraHoursWrkd = int(input("Insert total overtime worked: "))
  overtimePaym = extraHoursWrkd * (hourPaym * 1.5)
  regTimePaym = ttlRegHrsWrkd * hourPaym
  totalWeeklyPaym = regTimePaym + overtimePaym

  print("Weekly total pay: ", totalWeeklyPaym)

if __name__ == "__main__":
  main()
