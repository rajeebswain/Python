# Set Methods:
### Union: 
##### It prints all items that are present inthe two seta.
```
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
```
#### Output:
```
{1, 2, 3, 5, 6, 7}
```
### Untouched:
```
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1, s2)
```
#### Output:
```
{1, 2, 5, 6} {3, 6, 7}
```
##### Update: adds item into the existing set from another set
```
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)
```
#### Output:
```
{'Delhi', 'Berlin', 'Kabul', 'Madrid', 'Seoul', 'Tokyo'}
```
### Intersection and intersection_update():
##### These methods prints only items that are similar to both the sets.
##### The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
```
#### Output:
```
{'Madrid', 'Tokyo'}
```
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```
#### Output:
```
{'Madrid', 'Tokyo'}
```
### symmetric_difference() and symmetric_difference_update()
##### The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
##### The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```
#### Output:
```
{'Kabul', 'Berlin', 'Seoul', 'Delhi'}
```
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```
#### Output:
```
{'Kabul', 'Seoul', 'Delhi', 'Berlin'}
```
### difference() and difference_update()
##### The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets.
##### The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```
##### Output:
```
{'Madrid', 'Berlin', 'Tokyo'}
```
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```
#### Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
```


### isdisjoint:
##### This isdisjoint() method checks if items of given set are present in another set.
##### This method returns False if items are present, else it returns True.
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```
#### Output:
```
False
```
### issuperset():
##### The issuperset() method checks if all the items of a particular set are present in the original set.
##### It returns True if all the items are present, else it returms False.
```
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
```
#### Output:
```
False
False
```
### issubset():
##### The issubset() method checks if all the items of the original set are present in the particular set.
