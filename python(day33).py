# -*- coding: utf-8 -*-
"""Python(Day33).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I2OhdM0UtcvwIvf_95u6HFjUX2g8fj_H
"""

#What is the output of the following code?

for x in range(0, 5):

    print(x)

#What is true about this code?
value1 = 5 ** 2
value2 = "5 * 3"
print(value1, value2)
type(value2)

#What is true about the following code? Multiple answers

for number in range(10, 18, 2):
     print(number)

#What is true about  the following code? Multiple Answers

students=['Mohan', 'John', 'Ramesh', 'Mohan', 'John']
print("List of Students:", students)
team=tuple(students)
print("The team has:",team)

#What is the output of the following code?

sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)

#The following code does not work.  . Write code that works below when a =  2  and when a = 400.  Write the code in this canvas essay section.

a = 2
b = 330
if a > b:
  print(a)

else:
  print(b)

a = 400
b = 330
if a > b:
  print(a)

else:
  print(b)

#What is the output of

a = 200

b = 33

c = 500

if a > b and c > a:

    print("Both conditions are True")

else:

    print("200>33 and 500>200")

#What is true about the output of

fruits = ["apple", "banana", "cherry"]

for x in fruits:



        print(x)

#What is true about the following code? multiple answers

adj = ("red", "yellow")
fruits = ("apple", "banana")
for x in adj:
   for y in fruits:
      print(x, y)
type(y)

#What is the output of

adj = ["red", "yellow"]
fruits = ["apple", "banana"]
for x in fruits:
     if x=="apple": print(adj[0], x)
     else: print(adj[1], x)

#What is the output of the following code?

sampleList = ["Jon", "Kelly", "Jessa"]

sampleList.insert(2, "Scott")

print(sampleList)

#What is the output of

set1 = {'b', 'g', 'd', 'e', 'b'}

print(sorted(set1))

#What is the result of this program:

Friday = False
if Friday:
     print ("Casual day!")
else:
     print ("Dress code")

#What is true about the result of the following code?

groceries = ("eggs", "bread", "milk")

print (groceries[-1])

#What type of collection is {'a', 'b', 'c'}?
x={'a', 'b', 'c'}
print(x)
type(x)

#Store the names of three of your friends in a list called names.  Then use a for loop to print a message to each of them. The text of each message should be the same, but each message should include the person’s name.

#Write the code with 3 ways to do format the print statement.

#f-statement
names=['Safalta','Shrishan','Kalpana']
for name in names:
  print(f"Hi {name}!I miss you so much!")

#plus(+)
names=['Safalta','Shrishan','Kalpana']
for name in names:
  print("Hi " +name+"! I miss you so much!")

#comma(,)
names=['Safalta','Shrishan','Kalpana']
for name in names:
  print("Hi",name,"! I miss you so much!")

#Read the following code. Explain what each line is doing.   I am expecting you to write something like:
#Creating a list called animals with 6 items.
#----------------------------------------------------------------------------------------------------
animals=["monkey", "dog", "cat", "donkey", "bird", "deer"]
animals2=[]
for animal in animals[:]:
  if len(animal)==3:
    animals.remove(animal)
    animals2.append(animal)

  else:
    continue
  print(f'this is {animals}')
  print(f'this is {animals2}')

#Create an if-elif-else chain that prints three messages:  "low" if a number is between 0 and 10, "middle" if the number is between 10 and 20, and "high" if the number is greater than 20.
number=1
if 0<number<10:
  print("low")
elif 10<number<20:
  print("middle")
else:
  print("high")

#Now create a list of three numbers with one number between 0 and 10, another number between 10 and 20, and the third number greater than 20.
list_of_numbers=[8,13,21]

#Now create a for loop that loops through the list and prints the three messages according to the  if-elif-else chain.
for numbers in list_of_numbers:
  if 0<numbers<10:
    print("low")
  elif 10<numbers<20:
    print("middle")
  else:
    print("high")

#1.) Letting the user choose when to quit:
msg = ""
while msg != 'quit':
  msg = input("Enter your message ")
print(msg)

#2.) Using a active or flag to exit by changing the condition to false:
prompt = "Enter your message "
active= True
while active:
  msg = input(prompt)
  if msg == 'quit':
    active = False
  else:
    print(msg)

#3.)Using break to stop even when the condition is true:
prompt = "Enter your message "
while True:
  msg = input(prompt)
  if msg == 'quit':
    break
  else:
    print(msg)

#4.Using continue to stop the current iteration, and continue with the next:
number = 0
while number < 20:
  number += 1
  if number % 2 == 0:
    continue
  print(number, end =' ')