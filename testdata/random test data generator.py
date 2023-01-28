# write a function to  generate email addresses randomly in python with 8 string characters combinations of lowercase and integers ending with @gmail.com using random module
import random

def random_email():
    # generate a random string of 8 characters
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
    # generate a random integer ending with @gmail.com limit to 2 characters
    random_int = ''.join(random.choices('0123456789', k=2))
    # concatenate the random string and random integer
    random_email = random_string + random_int + '@gmail.com'
    return random_email

em = random_email() # call the function and assign the returned value to a variable
print(em) # print the result




