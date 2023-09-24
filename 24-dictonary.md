# Dictionaries:
##### These are ordered collection of data items.
### Example:
```
dic = {
    "Harry": "Human being",
    "Spoon": "Object"
}
print(dic["Harry"])
```
##### Output:
```
Human being
```

### Accessing Single & Multiple value
```
info = {'name':'Karan', 'age':'19', 'eligible':'true'}
print(info)
print(info['name'])
print(info.get('name'))
print(info.values())
```
#### Output:
```
{'name': 'Karan', 'age': '19', 'eligible': 'true'}
Karan
Karan
dict_values(['kiran', 19, True])
```
### Accessing Keys:
```
info = {'name':'Karan', 'age':'19', 'eligible':'true'}
print(info)
print(info['name'])
print(info.get('name'))
print(info.keys())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
```
#### Output:
```
{'name': 'Karan', 'age': '19', 'eligible': 'true'}
Karan
Karan
The value corresponding to the key name is Karan
The value corresponding to the key age is 19
The value corresponding to the key eligible is true
dict_keys(['name', 'ahe', 'eligible'])
```
### Accessing Key-value pairs:
```
info = {'name':'karan', 'age':19, 'eligible':True}
print(info.items())
for key, value in info.items():
    print(F"The value corresponding to the key {key} is {value}")
```
#### Output
```
    dict_items([('name', 'karan'), ('age', 19), ('eligible', True)])
The value corresponding to the key name is karan
The value corresponding to the key age is 19
The value corresponding to the key eligible is True
```