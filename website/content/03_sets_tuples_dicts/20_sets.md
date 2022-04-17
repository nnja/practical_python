+++
title = "Sets"
date = 2020-08-29T16:54:39-07:00
weight = 20
+++

A `set` is a mutable datatype that allows you to store **immutable** types in an **unsorted** way. Sets are mutable because you can add and remove items from them. They can contain immmutable items, like `tuple`s and other primitive types, but not `list`s, `set`s, or `dict`ionaries which are themselves mutable.

Unlike a list or a tuple, a set can only contain one instance of a unique item. There are no duplicates allowed.

The benefits of a set are: very fast membership testing along with being able to use powerful set operations, like `union` and `intersection`. 

### `set` cheat sheet

| type               	| `set`                                                                                                                         	|
|--------------------	|-------------------------------------------------------------------------------------------------------------------------------	|
| use                	| Used for storing immutable data types uniquely. Easy to compare the items in `set`s.                                          	|
| creation           	| `set()` for an empty set (`{}` makes an empty `dict`) and `{1, 2, 3}` for a set with items in it                              	|
| search methods     	| `item in my_set`                                                                                                              	|
| search speed       	| Searching for an item in a large set is very fast.                                                                            	|
| common methods     	| `my_set.add(item)`, `my_set.discard(item)` to remove the item if it's present, `my_set.update(other_set)` 	|
| order preserved?   	| **No**. Items *can't* be accessed by index.                                                                                   	|
| mutable?           	| **Yes**. Can add to or remove from `set`s.                                                                                    	|
| in-place sortable? 	| **No**, because items aren't ordered.                                                                                                                        	|
### Examples

#### Empty `set`s

Let's create our first few sets.

The first thing we might try to do is create an empty set with `{}`, but we'll come across a hurdle.

```python
>>> my_new_set = {}
>>> type(my_new_set)
<class 'dict'>
>>> my_set = set()
>>> type(my_set)
<class 'set'>
```

{{% notice info %}}
You can't create an empty `set` with `{}`. That creates a `dict`. Create an empty set with `set()` instead.
{{% /notice %}}

{{% notice tip %}}
While you're learning Python, it's useful to use `type()`, `dir()` and `help()` as often as possible.
{{% /notice %}}

#### `set`s with items

Now, let's make a new `set` with some items in it, and test out important `set` concepts.

#### `set`s can't contain duplicate values

```python
>>> numbers = {3, 3, 2, 2, 1}
>>> numbers
{1, 2, 3}
```

#### `set`s can be used to de-duplicate the items in a list

Tip: Use this to your advantage when you need to quickly deduplicate the items in a `list` *if you don't care about order*. Pass the `list` into the `set` constructor.

```
>>> names = ['Nina', 'Max', 'Nina']
>>> set(names)
{'Nina', 'Max'}
```

#### `set`s can't contain mutable types

You can consider a set to behave a lot like a dictionary that only contains keys (and no values). The way that `set`s allow you to quickly check if an item is contained in them or not is with an algorithm called a hash. I won't cover the details, but an algorithm is a way of representing an immutable data type with a unique numerical representation. An immutable data type is one where the contents can't be changed after creation.

If you're not sure if a type or an object is hashable, you can call the built-in `hash()` function on it. 

```python
>>> hash("Nina")
3509074130763756174
>>> hash([1, 2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

{{% notice info %}}
You'll see a `TypeError: unhashable type: 'list'` if you try to add a mutable data type (like a `list`) to a set.
{{% /notice %}}

If you try to add a mutable data type (like a `list`) to a set, you'll see the same `TypeError`, complaining about an `unhashable type`.

```python
>>> {"Nina"}
{'Nina'}
>>> {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

#### `set`s don't have an order

Sets don't have an order. That means that when you print them, the items won't be displayed in the order they were entered in the set.

```python
>>> my_set = {1, "a", 2, "b", "cat"}
>>> my_set
{1, 2, 'cat', 'a', 'b'}
```

It also means that you *can't* access items in the `set` by position in subscript `[]` notation.

```python
>>> my_set = {"Red", "Green", "Blue"}
>>> my_set[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

{{% notice info %}}
You'll see `TypeError: 'set' object does not support indexing` if you try to access the items in a `set` by index with `my_set[pos]`
{{% /notice %}}

Tip: If your set contains items of the same type, and you want to sort the items, you'll need to convert the `set` to a `list` first.

Or, you can use the built-in `sorted(sequence)` method, which will do the conversion for you.

```python
>>> my_set = {"a", "b", "cat", "dog", "red"}
>>> my_set
{'b', 'red', 'a', 'cat', 'dog'}
>>> sorted(my_set)
['a', 'b', 'cat', 'dog', 'red']
```

#### adding to and removing from `set`s

Since a set has no order, we can't add or remove items to it by index.

Instead, the operations are called with items.

##### Add items to a set with `my_set.add(item)`.

```python
>>> colors = {"Red", "Green", "Blue"}
>>> colors.add("Orange")
>>> colors
{'Orange', 'Green', 'Blue', 'Red'}
```

##### Remove items with `my_set.discard(item)`

You can remove an item from a `set` if it's present with `my_set.discard(item)`. If the set doesn't contain the item, no error occurs.

```python
>>> colors = {"Red", "Green", "Blue"}
>>> colors.discard("Green")
>>> colors
{'Blue', 'Red'}
>>> colors.discard("Green")
>>> colors
{'Blue', 'Red'}
```

You can also remove items from a `set` with `my_set.remove(item)`, which will raise a `KeyError` if the item doesn't exist.

##### Update a set with another sequence using `my_set.update(sequence)`

You can add to the items in a `set` by passing in another sequence such as a `set`, `list`, or `tuple` to the `update()` method.

```python
>>> colors = {"Red", "Green"}
>>> numbers = {1, 3, 5}
>>> colors.update(numbers)
>>> colors
{1, 3, 'Red', 5, 'Green'}
```

{{% notice info %}}
Be careful passing in a `str`ing to `my_set.update(sequence)`. That's because a `str`ing is a sequence of characters under the hood.
{{% /notice %}}

```python
>>> numbers = {1, 3, 5}
>>> numbers.update("hello")
>>> numbers
{1, 3, 'h', 5, 'o', 'e', 'l'}
```

Your set will update with each character of the `str`ing, which was probably not your intended result.

### `set` operations

`set`s allow quick and easy operations to compare items between two `set`s.

#### `set` operations cheat sheet

 method operation    	| symbol operation 	| result                                                                        	|
|---------------------	|------------------	|-------------------------------------------------------------------------------	|
| `s.union(t)`        	| <code>s &#124; t</code> | creates a new `set` with all the items **from both `s` and `t`**             |
| `s.intersection(t)` 	| `s & t`          	| creates a new `set` containing *only* items that are **both in `s` and in `t`** 	|

#### Examples

Let's see it in action.

We have two sets, `rainbow_colors`, which contain the colors of the rainbow, and `favorite_colors`, which contain my favorite colors.

```python
>>> rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
>>> favorite_colors = {"Blue", "Pink", "Black"}
```

First, let's combine the sets and create a new `set` that contains all of the items from `rainbow_colors` and `favorite_colors` using the union operation. You can use the `my_set.union(other_set)` method, or you can just use the symbol for union `|` from the table above.

```python
>>> rainbow_colors | favorite_colors
{'Orange', 'Red', 'Yellow', 'Green', 'Violet', 'Blue', 'Black', 'Pink'}
```

Next, let's find the intersection. We'll create a new `set` with *only* the items in both `set`s.

```python
>>> rainbow_colors & favorite_colors
{'Blue'}
```

There are other useful operations available on `set`s, such as checking if one set is a subset, a superset, differences, and more, but I don't have time to cover them all. Python also has a `frozenset` type, if you need the functionality of a `set` in an immutable package (meaning that the contents can't be changed after creation).

Find out more by reading the [documentation](https://docs.python.org/3/library/stdtypes.html#set), or calling `help()` on `set`.
