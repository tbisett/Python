# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

for x in students:
    for y in x:
        if x.get(y) == 'Jordan':
            x.update({y: "Bryant"})
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

for x in z:
    for y in x:
        if x.get(y) == 20:
            x.update({y: 30})
print(z)

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(len(students1)):
        print(f"first_name - {students1[i]['first_name']}, last_name - {students1[i]['last_name']}")

iterateDictionary(students1)


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(students1)):
        print(students1[i][key_name])

iterateDictionary2('first_name', students1)
iterateDictionary2('last_name', students1)

# Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(key_name, some_dict):
    print(f"{len(some_dict[key_name])} {key_name}")
    for i in range(len(some_dict[key_name])):
        print(some_dict[key_name][i])

printInfo('locations', dojo)
printInfo('instructors', dojo)







