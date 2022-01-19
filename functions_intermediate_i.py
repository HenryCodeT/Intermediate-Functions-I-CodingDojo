# 1-Update values ​​in dictionaries and lists
x = [ [ 5 , 2 , 3 ], [ 10 , 8 , 9 ] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
     'basketball' : [ 'Kobe' , 'Jordan' , 'James' , 'Curry' ],
     'football' : [ 'Messi' , 'Ronaldo' , 'Rooney' ]
}
z = [ {'x': 10 , 'y' : 20 } ]

# 1.1-Change
print('********** 1.1-Change **********')
x[1][0]=15
print(x)

# 1.2-change de first student last name
print('********** 1.2-change de first student last name **********')
students[0]["last_name"]="Bryant"
print(students)

# 1.3-In the sports_directory, change "Messi" to "Andrés".
print('********** 1.3-In the sports_directory, change "Messi" to "Andrés" **********')
sports_directory['football'][0]='Andres'
print(sports_directory)

# 1.4-Change the value 20 to za 30.
print('********** 1.4-Change the value 20 to za 30 **********')
z[0]['y']=30
print(z)

#2-Iterate through a list of dictionaries
print('********** 2-Iterate through a list of dictionaries **********')
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
     newstring = ''
     for i in some_list:
          newstring +='first_name - %s, last_name %s \n' %(i['first_name'],i['last_name'])
     return newstring

# should return: (it's fine if each key-value pair ends on 2 separate lines; 
# a bonus for them to appear exactly as shown below) 
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
result = iterateDictionary(students)
print(result)

# 3-Get values ​​from a list of dictionaries
print('********** 3-Get values ​​from a list of dictionaries **********')
def iterateDictionary2(key_name, some_list):
     newstring=''     
     for i in some_list:
          newstring += '%s \n'%(i[key_name])
     return newstring
result1 =iterateDictionary2('first_name', students)
print(result1)
result2 =iterateDictionary2('last_name', students)
print(result2)

# 4-Iterate through a dictionary with list values
print('********** 4-Iterate through a dictionary with list values **********')
dojo = {
    'locations' : [ 'San Jose' , 'Seattle' , 'Dallas' , 'Chicago' , 'Tulsa' , 'DC' , 'Burbank' ],
    'instructors' : [ 'Michael' , 'Amy' , 'Edward' , 'Josh' , 'Graham' , 'Patrick' , 'Minh' , 'Devon' ]
}
def printInfo(dojo):
     newstring=''
     for i in dojo:
          newstring += f'\n{len(dojo[i])} {i.upper()} \n'
          for i in dojo[i]:
               newstring +=f'{i} \n'
     return newstring

print(printInfo(dojo))
 # output: 
# 7 LOCATIONS
# Saint Joseph
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# bright
# Devon
