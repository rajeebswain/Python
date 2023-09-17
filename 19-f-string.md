# f-string
### Case-1
```
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Rajiv"
print(letter.format(name, country))
```
#### Output:
```
Hey my name is Rajiv and I am from India
```
##### The declared variable "name" and "country", printed in the placce of curly bracket in the print statment.

### Case-2
##### if we change the place of variable in print sttement during passing , the location of the variable will change in the output too. 
##### And we will not get the desired output.
```
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Rajiv"
print(letter.format(country, name))
```
##### Output:
```
Hey my name is India and I am from Rajiv
```
### Case-3
##### We can assign the index number to overcome from above issue.
```
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rajiv"
print(letter.format(country, name))
```
#### Output:
```
Hey my name is India and I am from Rajiv
```
### Case-4
##### The above process is not a good approach, when we have a lot of variable. 
##### We can add the variavle name direct in print, by declaring as f-string.
```
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rajiv"
print(f"Hey my name is {name} and I am from {country}")
```
#### Output:
```
Hey my name is Rajiv and I am from India
```
### Case-5
##### It will print upto 2 decimal.....
```
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999))
```
#### Output:
```
For only 49.10 dollars!
```
### Case-6
##### Convert into f-string
```
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
```
#### Output:
```
For only 49.10 dollars!
```
### Case-7
##### making a f-string
```
print(f"{2*30}")
```
#### Output:
```
60
```

### Case-8
##### If we want to renain or display f-string in output, then use double {}.
```
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rajiv"
print(f"Hey my name is {{name}} and I am from {{country}}")
```
#### Output:
```
Hey my name is {name} and I am from {country}
```