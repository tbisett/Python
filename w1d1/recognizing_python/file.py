num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# lines 1-7 = declaring variables/lists    line 8 = printing out what kind of data type it is(list)   line 9 = outputting index 1 from pizza_toppings list  
# line 10 = adding string "mushrooms" to the end of the pizza toppings list  line 11 = output name index of person list  line 12-13 = replacing the values of the particular list index
#  output index 2 of the fruit list


if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# printing out different strings depending on a condition

for x in range(5):    
    print(x)
for x in range(2,5):   
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
# declaring for loops with range
# declaring for loops with range and argument (start at 2 end at 5)
# declaring for loops with range and argument (start at 2, end at 10, iterate by 3)
# while loop(while x is less than 5 print x, then increase x by 1)

pizza_toppings.pop()
pizza_toppings.pop(1)
# removing the last index of pizza toppings list
# removing index 1 of pizza toppings list

print(person)
person.pop('eye_color')
print(person)
# outputting person list, removing 'eye color' index of person list, outputting again

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# if statement that states; if topping equals pepperoni, continue loop, output 'After 1st if statement', if topping equals olives break the loop
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# defining functions that will print a string a certrain amount of times depending on the paramaters of the function
print_hello_x_or_ten_times() 
# prints hello ten times
print_hello_x_or_ten_times(4)
# prints hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)

# declaring variables/ data types, printing values from index in library, adding raspberry to the end of fruit list, removing index 1 of fruit list.