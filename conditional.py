   #If statement

#check if a person is old enough to vote
age = int(input ("What is your age?"))

if age>18:
    print ("You are eligible to vote")
elif age<= 0:
    print ("You are not even born yet")
elif age> 150:      #You gotta change the order or do as follow
    print ("Hey are you alive?")
else:
    print ("Please wait a few more years to vote")

if age>18:
    if age>150:
    print ("heyy are you alive?")
    else:
    print ("You are eligible to vote")
elif age<= 0:
    print ("You are not even born yet")
else:
    print ("Please wait a few more years to vote")





 

#prompt the user to enter his password
user_password = input("Type a password")
nb_characters= len (user_password)

# check if the password is valid (more than 7 characters)
if nb_characters<7:
    print("heyy your password is too short!!!")
else: 
    print("Your password is valid")
    print ("your account can be created")