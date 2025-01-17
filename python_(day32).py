# -*- coding: utf-8 -*-
"""Python (Day32).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRuIDlayXN0Uc9d3KovMglS0YCyZy29d
"""

name1=['phil','joe','andy']
subusers=name1[0:2]
print(subusers)

for x in range(1,5):
  print(x)

name1=['phil','joe','andy']
name2=[]
while name1:
  user=name1.pop()  #pop throws the last item first unless you give it the posistion of the item like 0 or 1
  print(user)
  name2.append(user)
print(name1)
print(name2)

names = ['phil', 'sarah', 'erin','phil']
while 'phil' in names:
     names.remove('phil') #when you use remove, you can just use the value itself
print(names)

"""Question 1: Create a range"""

numbers = range(11)  # Numbers from 0 to 10
result_list = []

for number in numbers:
    incremented = number + 4
    final_result = incremented / 2
    result_list.append(final_result) #adds final result to empty list
    print(final_result)

print(result_list)

"""Countries"""

countries_5 = ["USA", "Canada", "UK", "Australia", "India"] #this code is comparing two lists
countries_2 = ["UK", "India", "China", "Germany"]
no_countries = []
for country in countries_2:
  if country in countries_5:
    print(f"{country} is in both lists.")
  else:
    no_countries.append(country)
print(f"\nTotal countries in countries_5: {len(countries_5)}")
print(f"Total countries in countries_2: {len(countries_2)}")
print(f"Total countries in no_countries: {len(no_countries)}")

if no_countries:
    print("\nCountries not in the list of 5 countries:")
    for country in no_countries:
        print(country)

"""Colors

"""

# Initialize the set and lists
colors_set = {"red", "blue", "green", "yellow", "orange", "red", "blue"} #it is a set becasue it has sqiuggly brackets - also this has duplicates but since sets can't have duplicates, when the program runs, it is just gonna ignore the duplicate items
red_colors = [] #we are turnng sets in to two lists is because sets cant be modified
blue_list = []

# Process colors - why do we have list() below??
for color in list(colors_set):
    if color == "red":
        colors_set.remove(color)
        red_colors.append(color)
    elif color == "blue":
        colors_set.remove(color)
        blue_list.append(color)
    else:
        print(f"{color} not red or blue.")

# Count the items
red_count = len(red_colors)
blue_count = len(blue_list)
set_count = len(colors_set)

# Print messages
print(f"The red_colors list has {red_count} items: {', '.join(red_colors)}.") #here  {', '.join(red_colors)} means take whatever is in this list, take it and put a comma in between them. if you want to print + instead of , it's ok.
print(f"The blue_list has {blue_count} items: {', '.join(blue_list)}.")#join is just a way of presenting list without the brackets
print(f"The colors_set has {set_count} items: {', '.join(colors_set)}.")

colors = ["red", "blue", "green", "yellow", "orange", "red", "blue"]
colors2=[]
for color in colors[:]:
  print(color)
  x = colors.pop()
  print(color)
  colors2.append(x)

print(colors)
print(colors2)



"""Sets"""

# Initialize the set and lists
colors_tup = ("red", "blue", "green", "yellow", "orange", "red", "blue")
print(colors_tup)
red_colors = []
blue_list = []
blue_counter = 0
red_counter = 0
# Process colors
for color in colors_tup:
    if color == "blue":
        blue_counter += 1

    elif color == "red":
        red_counter += 1

# Count the items
print("blue =", blue_counter)
print("red =",red_counter)
print(sorted(colors_tup))

colors_set = ["red", "blue", "green", "yellow", "orange", "red", "blue"]
colors=[]
for color in colors_set[:]:
  x = colors_set.pop()
  colors.append(x)

print(colors_set)
print(colors)

colors_set = ["red", "blue", "green", "yellow", "orange", "red", "blue"]
colors=[]
for color in colors_set[:]:
  colors_set.remove(color)
  colors.append(color)

print(colors_set)
print(colors)

colors_set = ["red", "blue", "green", "yellow", "orange", "red", "blue"]
colors=[]
while colors_set:
  x = colors_set.pop()
  colors.append(x)

print(colors_set)
print(colors)

#program where we have a list of numbers, if even move it to another list called even, if odd move it to another list called odd
numbers = range(11)  # Numbers from 0 to 10
even_numbers = []
odd_numbers =[]

for number in numbers:
  if number % 2==0:
    even_numbers.append(number)
  else:
    odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)