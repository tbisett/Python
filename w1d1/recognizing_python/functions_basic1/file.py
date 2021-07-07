#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# going to print 5, since the value returned to the function is 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# error, since no value is given to the first function

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# print 10 since 10 is the latter value returned to the function

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# print 5 because the return stops the loop/function before it prints 10

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#probably 5 then an error because x is already given the value of the function

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# print 5 and 3 since the function prints and is called twice. dont think you can add two functions

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#11
b = 500
print(b)
def foobar():
    b ="keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

