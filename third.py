#Third excercise
#Input function asks for a integer number: Prints out and enumerate Hello the number of times given in the input.
def print_hello(count):
  for i in range(1, count+1):
      print(f"{i}. Hello")

def convert_to_number(num):
  num = int(num)
  return num
  
try:
    num = input("Write a integer number: ")
    print_hello(convert_to_number(num))
except ValueError:
    print("Error: Input is not a number.")
