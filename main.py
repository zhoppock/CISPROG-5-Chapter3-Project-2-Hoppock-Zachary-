#enter the lengths of 3 sides of a triangle
firstSide = int(input("Enter length of first side of triangle: "))
secondSide = int(input("Enter length of second side of triangle: "))
thirdSide = int(input("Enter length of third side of triangle: "))
#square each number to be used in the calculation ahead
sqFirstSide = (firstSide ** 2)
sqSecondSide = (secondSide ** 2)
sqThirdSide = (thirdSide ** 2)
#determine if the triangle is a right triangle by calculating by the Pythagorean theorem
if sqFirstSide == (sqSecondSide + sqThirdSide):
  print("This is a right triangle!")
elif sqSecondSide == (sqFirstSide + sqThirdSide):
  print("This is a right triangle!")
elif sqThirdSide == (sqFirstSide + sqSecondSide):
  print("This is a right triangle!")
else:
  print("This is NOT a right triangle.")