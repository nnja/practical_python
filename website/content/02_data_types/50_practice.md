+++
title = "Practice"
date = 2020-08-29T16:53:35-07:00
weight = 50
pre = "<b>⭐️ </b>"
+++

## Basic Data Types, Strings and Numbers

### Types

List the type of the following variables using the `type()` function.

```python
>>> x = 42
>>> y = 3 / 4
>>> z = int('7')
>>> a = float(5)
>>> name = "Nina"
>>>
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(z)
<class 'int'>
>>> type(a)
<class 'float'>
>>> type(name)
<class 'str'>
```

### Helper Functions

In addition to `type()`, Python has a few other built-in functions to help you if you get stuck. `dir()` returns a list of valid attributes for an object, so you can quickly see what variables an object has or what functions you can call on it. `help()` brings up helpful documentation on any object. You can also type `help()` on its own to bring an interactive help console.

```python
>>> name = "Nina"
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
>>> help(name.upper)

Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
(END)
```

Remember to close the `help()` menu by pretting `q`

### Numbers

Calculate the amount of rent you pay daily, by taking your monthly rent and diving it by 30.

```python
>>> rent = 480
>>> per_day = rent / 30
>>> print(per_day)
16.0
```

### Strings

Try printing some things to your REPL:

```python
>>> print("Hello world")
Hello world
>>> name = "Nina"
>>> print("My name is", name)
My name is Nina
```

There are three different ways to format strings in Python3. You may run into %-formatting and `str.format()` in older code. These are still common in Python but no longer recommended, due to readability concerns.

```python
>>> name = "Nina"
>>> print("Hello, my name is %s" % name)
Hello, my name is Nina
```

The current recommended way to format string is with f-Strings. f-Strings are much more readable and easier to maintain than the previous methods. With f-Strings, your string is prepended with the letter `f` and your variables or expressions to interpret are placed in `{brackets}`.

```python
>>> name = "Nina"
>>> print(f"Hello, my name is {name} and I pay ${rent / 30} in rent per day")
Hello, my name is Nina and I pay $16.0 in rent per day
```
<!--
### Helper Functions

Python has a few built-in functions to help you if you get stuck. `type()` tells you what an object's type is, for example a string (`str`) or integer (`int`). `dir()` returns a list of valid attributes for an object, so you can quickly see what variables an object has or what functions you can call on it. `help()` brings up helpful documentation on any object. You can also type `help()` on its own to bring an interactive help console.

```python
>>> x = 42
>>> y = 3 / 4
>>> name = "Nina"
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(name)
<class 'str'>
```
-->

### Lists

Lists are great for storing an ordered sequence of objects. Remember that you can see the current state of your list at any time by typing the name of your list by itself. Check your list after every operation to see if it has changed.

```python
>>> my_list = ["h", "e", "l", "l", "o"]
# Let's look at our list:
>>> my_list
# Let's add to my_list:
>>> my_list.append("!")
# Now let's see it again:
>>> my_list
```

There are many other ways to interact with our lists as well:

```python
# Remove the first L:
>>> my_list.remove("l")
# Let's put it back at index 2
>>> my_list.insert(2, "l")

# Delete any element
>>> del my_list[0]
# Remove and return the last element. Useful for queues!
>>> last_item = my_list.pop()
>>> last_item

# We can also look at individual items my using an index:
>>> my_list[2]
# Or we can see if a certain value exists in the list:
>>> "!" in my_list
# Let's sort our list in reverse order
>>> my_list.sort(reverse=True)
>>> my_list
# Note that sort() doesn't return anything, it sorts the list in-place
# You can also use the sorted() function to return a new, sorted list without modifying the old one
>>> sorted(my_list, reverse=False)
>>> my_list
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = ["h", "e", "l", "l", "o"]
>>> my_list
['h', 'e', 'l', 'l', 'o']
>>> my_list.append("!")
>>> my_list
['h', 'e', 'l', 'l', 'o', '!']

>>> len(my_list)
6
>>> my_list[4:6]
['o', '!']
>>> my_list[4:]
['o', '!']
>>> my_list[-2:]
['o', '!']

>>> my_list.remove("l")
>>> my_list.insert(2, "l")
>>> del my_list[0]
>>> last_item = my_list.pop()
>>> last_item
'o'
>>> my_list[2]
'l'
>>> "!" in my_list
False
>>> my_list.sort(reverse=True)
>>> my_list
['o', 'l', 'l', 'h', 'e', '!']
>>> sorted(my_list, reverse=False)
['!', 'e', 'h', 'l', 'l', 'o']
```

{{% /expand%}}