# Sets:
##### It doesn't print repeated value.
#####  Sets are unchageable. 
##### Sets are unordered collection of data items.
```
s = {2, 4, 2, 6}
print(s)
```
#### Output:
```
{2, 4, 6}
```
```
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 'Carla', 19, 5.9}
```
##### If we try to write an empty set with curly bracket, that become a dictonary.
```
rajiv = {}
print(type(rajiv))
```
#### Output:
```
<class 'dict'>
```
##### How to declare or write an empty set.
```
rajiv = set()
print(type(rajiv))
```
#### Output:
```
<class 'set'>
```
##### We can write set with for loop.
```
info = {"Carla", 19, False, 5.9, 19}
for value in info:
     print(value)
```
#### Output:
```
False
19   
5.9  
Carla
```

