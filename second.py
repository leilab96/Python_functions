#Second excercise
#A function that counts a certain element in a list and returns with the repeats
names=['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']

def count_element(my_list, element):
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    if count == 0:
      print("No element was found!")
    else:
      print(f"{element} is present in the list {count} times.")
    return count
  
count_element(names, 'Pista')
count_element(names, 'Anna')