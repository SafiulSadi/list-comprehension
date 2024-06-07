numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(numbers)
print(new_list)
# sequences
# range(1, 5)
a = range(1,5)
new_list = [n*2 for  n in range(1, 5)]
print( new_list)
# new_list  =  [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = ["hi, " + name for name in names if len(name)< 5]
print(names)
print(short_names)
uppercase_names = [name.upper() for name in names if len(name)>=5]
print(uppercase_names)