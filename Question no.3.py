# string_name = "Shakrudin"
# print (len(string_name)) 

# string_name = "Rishabh Verma"
# print (len(string_name)) 

# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai") 
# string_name="n"
# print (n in string_name)
# print (type(n in string_name) )

import json
with open('user.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in data:
  counter = 0
  print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
  while counter < len(user['details']):
    print ("users mobile number is " + user['details'][counter]['mobileNo'])
    print ("users age  is " + user['details'][counter]['age'])
    print ("users city is " + user['details'][counter]['city']) 

