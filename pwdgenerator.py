# the random module allows random selection of values
import random

print("welcome to password generator 1.0 Follow the instructions to generate random passwords") #welcome message
print('\n')
password_number = input("how many passwords do you want to generate ? ") #stores the number of passwords required
password_number = int(password_number)

print('\n')

password_length = input("What is your preffered password length  ? ") #stores the required password length
password_length = int(password_length)

char_options = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' #the characters used to make up the password 

passwords = [] #holds the generated passwords
for _ in range(password_number): #loops through the number of passwords specified
    password = ''
    for _ in range(password_length):#loops through the password length specified
        password += random.choice(char_options) #randomly selects characters from the char_options string
    passwords.append(password)

print("Success!! the following passwords have been generated")
for password in passwords: #prints the generated passwords
    print(password)