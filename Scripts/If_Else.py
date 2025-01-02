#This program converts from Celsius to Fahrenheit

user_response = input ("please input a temperature in Celsius : ")
celsius = float (user_response)
fahrenheit = ((celsius*9)/5)+32
if fahrenheit > 90:
    print ("It is hot")
else:
    print("It is no hot")
print(fahrenheit)
