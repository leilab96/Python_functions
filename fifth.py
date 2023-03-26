#Fifth excercise
#List of names is sorted and splitted into two groups
def sort_and_split(names):
    sorted_names = sorted(names)
    middle = len(sorted_names) // 2
    #if the length of the list is odd there will be 1 more person in the second group
    first_half = sorted_names[:middle]
    second_half = sorted_names[middle:]
    print("1. csoport:")
    print(first_half)
    print("2. csoport:")
    print(second_half)

names=['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
sort_and_split(names)
names.append('Faragó Anikó')
sort_and_split(names)