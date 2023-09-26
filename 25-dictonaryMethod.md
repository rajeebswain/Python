# Dictonary Method

## Note: Set is un-ordered but dictonary is ordered.

### update(): It will update the dictonary with new key-vale pairs.
```
ep1 = {122:45, 123:89, 567:69, 670: 69}
ep2 = {122:67, 566:90}

ep1.update(ep2)
print(ep1)
```
#### Output
```
{122: 67, 123: 89, 567: 69, 670: 69, 566: 90}
```
### clear(): It will print an empty dictonary.
```
ep1 = {122:45, 123:89, 567:69, 670: 69}
ep2 = {122:67, 566:90}

ep1.clear()
print(ep1)
```
#### Output:
```
{}
```
### pop(): It removes the mentioned first key-value pair.
```
ep1 = {122:45, 123:89, 567:69, 670: 69}
ep2 = {122:67, 566:90}

ep1.pop(122)
print(ep1)
```
#### Output:
```
{123: 89, 567: 69, 670: 69}
```
### popitem(): It removes the last key-value pair from the dictionary.
```
ep1 = {122:45, 123:89, 567:69, 670: 69}
ep2 = {122:67, 566:90}

ep1.popitem()
print(ep1)
```
#### Output:
```
{122: 45, 123: 89, 567: 69}
```
### del: It delete the entire dictionary item.
```
ep1 = {122:45, 123:89, 567:69, 670: 69}
del ep1
del ep1[122]
print(ep1)
print(ep1)
```
#### Output:
```
It will throw an error, as ep1 not defined. Here it will delete entire ep1. 
{123: 89, 567: 69, 670: 69}: It it deleted only one key-value pair.
```
