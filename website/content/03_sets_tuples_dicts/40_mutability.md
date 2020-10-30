+++
title = "Mutability"
date = 2020-08-29T16:55:00-07:00
weight = 40
+++

### Mutability

Mutability, simply put: the contents of a mutable object can be changed, while the contents of an immutable object cannot.

### Simple Types

All of the simple data types we covered first are **immutable**. 

You can replace the value, but you can't change it.

| type                      	| use                     	| mutable? 	|
|---------------------------	|-------------------------	|----------	|
| `int`, `float`, `decimal` 	| store numbers           	| **no**   	|
| `str`                     	| store strings           	| **no**   	|
| `bool`                    	| store `True` or `False` 	| **no**   	|

### Container Types

For the mutability of the container types we covered next, check this helpful list:

| container type 	| use                                                                                                     	| mutable? 	|
|----------------	|---------------------------------------------------------------------------------------------------------	|----------	|
| `list`         	| ordered group of items, accessible by position                                                          	| **yes**  	|
| `set`          	| mutable unordered group consisting only of immutable items. useful for set operations (membership, intersection, difference, etc) 	| **yes**  	|
| `tuple`        	| immutable collection containing ordered groups of items                                         	| **no**   	|
| `dict`         	| contains key value pairs                                                                                	| **yes**  	|
