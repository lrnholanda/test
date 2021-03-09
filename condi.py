cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else:
        print(car.title())    
 
 

  
  #exemplo 2
requested_topping = 'mushrooms'
if requested_topping != ' anchovies':
      print("Hold the anchovies!")
      
#exemplo 3

answer = 17
if answer != 13:
    print("That is not the correct answer. Please try again!")
    
#exemplo 4

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    