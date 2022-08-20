import math

def main():

  radius = float(input("Enter the radius: "))
  diameter = radius * 2
  circumf = math.pi * 2 * radius
  area = math.pi * (radius * radius)
  vol = 4/3 * math.pi * (radius * radius * radius)

  print("Diameter: ", diameter, "\nCircumference: ", circumf, "\n Area: ", area, "\nVolume: ", vol)

if __name__ == "__main__":
  main()
