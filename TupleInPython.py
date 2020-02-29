ages=(2,12,13,45,90,34,2)#this is a tuple. no data can be added in this tupple
#tupples have rounded brackets and lists are used in conjuction with square brackets
#ages.add (X) DOESNT WORK
print(ages)
print(ages[2:3])#prints only the third  element(index 2)

#months of the year (which generally should not change
months_of_the_year_tuple = ('January', 'February', 'March', 'April', 'May', 'June',
                             'July', 'August', 'September', 'October', 'November', 'December')
#looping through a tuple
for i in months_of_the_year_tuple:
  print(i)

#this lines converts tuples into lists
months_of_the_year_list = list(months_of_the_year_tuple)
print('months_of_the_year_tuple is {}.'.format(type(months_of_the_year_tuple)))
print('months_of_the_year_list is {}.'.format(type(months_of_the_year_list)))

#converting tuples to lists
animals = ['hen','goat', 'chicken']
print("animal is a {}".format(type(animals)))
animals_list = tuple(animals)
print("animals list is a {}".format(type(animals_list)))


year_list = [22, 21, 34, 56, 67, 87, 67 ]

print(year_list)
year_list.append(12)   #adding more data to the years list at the end
print(year_list)
year_list.insert(2,39)  #inserts data at a specific point i.e position 2 the data is 39
print(year_list)

print("splitting")
message=("welcome to 101 python project")

words=message.split("101")

print(words[0:1])

print(message)