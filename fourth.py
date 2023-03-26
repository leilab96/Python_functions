#Fourth excercise
# calculating and displaying ( with 2 decimal places) the circumference and area of a circle with a given radius
import math

def convert_to_number(num):
  num = float(num)
  return num

def circle_area(radius):
  area = math.pi * radius ** 2
  return area
5
def circle_circumference(radius):
  circumference = 2 * math.pi * radius
  return circumference  
  

try:
    radius = convert_to_number(input("Radius of the circle: "))
    print(f"Circumference of the circle is {circle_circumference(radius): .2f}")
    print(f"Area of the circle is {circle_area(radius): .2f}")
except ValueError:
    print("Error: Input is not a number.")