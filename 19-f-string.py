####### Case-1
# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Rajiv"
# print(letter.format(name, country))

# Output:
# PS F:\py\python> python f-string.py 
# Hey my name is Rajiv and I am from India

# Explanation:
# Here, the name and country placed in the {} in the print statment.

####### Case-2
# if we change the place of country and name, that will change in the print statement too. 

# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Rajiv"
# print(letter.format(country, name))

# Output:
# PS F:\py\python> python f-string.py
# Hey my name is India and I am from Rajiv

####### Case-3
# We can assign the index number to overcome from above issue.
# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Rajiv"
# print(letter.format(country, name))

# Output:
# PS F:\py\python> python f-string.py
# Hey my name is India and I am from Rajiv

####### Case-4
# The above process is not a good approach, when we have a lot of variable. 
# We can add the variavle name direct in print, by declaring as f-string.

# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Rajiv"
# print(f"Hey my name is {name} and I am from {country}")

# Output:
# PS F:\py\python> python f-string.py
# Hey my name is Rajiv and I am from India

####### Case-5
# It will print upto 2 decimal.....

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49.09999))

# Output:
# PS F:\py\python> python f-string.py
# For only 49.10 dollars!

####### Case-6
# Convert into f-string
# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)

# Output:
# PS F:\py\python> python f-string.py
# For only 49.10 dollars!

####### Case-7
# making a f-string
print(f"{2*30}")

# Output:
# 60

####### Case-8
# If we want to renain or display f-string in output, then use double {}.

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rajiv"
print(f"Hey my name is {{name}} and I am from {{country}}")

Output:
PS F:\py\python> python 19-f-string.py
Hey my name is {name} and I am from {country}