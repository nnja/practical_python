+++
title = "Practice"
date = 2020-08-29T16:59:09-07:00
weight = 50
+++

## Comprehensions

Let's practice our comprehensions. Create a list of only odd numbers between 0 and 100 using a list comprehension. Then, use a comprehension to create a dictionary where the keys are the even numbers from your list, and the values are random integers between 0 and 100 (hint: try `random.randint(min, max)`). Finally, use a comprehension to create a set of every unique value from the above dictionary.

```python
>>> my_list = [num for num in range(0, 100) if num % 2 == 0]
>>> print(my_list)

>>> import random
>>> my_dict = {num:random.randint(0, 100) for num in my_list}
>>> print(my_dict)

>>> my_set = {num for num in my_dict.values()}
>>> print(my_set)
```


### Slicing

Let's play with slices. How do we get the last two elements of our list?

```python
>>> my_list = ["h", "e", "l", "l", "o", "!"]
>>> len(my_list)
# So the last two indexes are 4 and 5. Since the first number in the slice is inclusive, and the second number is exclusive, we can ask for everything between index 4 and 6
>>> my_list[4:6]
# We can also say "Give me everything after index 4
>>> my_list[4:]
# Or, we can ask for just the last two items without caring how big the list is. This means "give me everything starting from two before the end":
>>> my_list[-2:]
```

You know how to create a list of even or odd numbers with a list comprehension. Make a list of numbers between 0 and 100, then try making a list of even numbers between 30 and 70, by taking a slice from the first list. Then, make a new list in the reverse order.

```python
>>> my_list = [num for num in range(0, 100)]
>>> my_slice = my_list[30:70:2]
>>> print(my_slice)
>>> my_backwards_slice = my_slice[::-1]
>>> print(my_backwards_slice)
```

### `zip`

Make a list of all the names you can think of, called "names". Make a second list of numbers, called "scores", using a list comprehension and `random.randint(min, max)` as before. Use the first list in your comprehension to make it the same length. Then, use `zip()` to output a simple scoreboard of one score per name.

```python
>>> names = ["Nina", "Max", "Floyd", "Lloyd"]
>>> scores = [random.randint(0, 100) for name in names]
>>> scores
[41, 38, 96, 81]
>>> for name, score in zip(names, scores):
...     print(f"{name} got a score of {score}")
...
```


## Converting Between Types

Converting between types in Python is one of the most powerful language features.

You can quickly convert between strings, numbers, and various data-types to supercharge quickly solving problems.
You can even use powerful data structures like sets to your advantage.

### Converting Between Numbers and Strings

Converting between numbers and strings is easy with `str()` and `int()`:

```python
>>> my_string = str(100)
>>> my_string
>>> type(my_string)
>>> my_int = int(my_string)
>>> my_int
>>> type(my_int)
```

You can also use `float()` to convert strings into floating point numbers:

```python
>>> float("3.1415")
3.1415
```

Bonus tip: `int()` works great for converting floats as well, as long as you don't care about the mantissa (the part after the decimal point):

```python
>>> int(3.1415)
```

### Converting Between Lists and Strings

A `str`ing can be considered as just a list of characters, so converting back and forth is easy:

```python
>>> my_list = list("hello")
>>> my_list
>>> str(my_list)
```

Oops, that wasn't quite what we wanted. Running any object through `str()` will usually return a literal string of that object. What we want is to *join* the elements of the list (into a string). We can do that using string's built-in `join()` method. In this case, we'll use an empty string:

```python
>>> ''.join(my_list)
# Note: we can use any string we want to join the characters!
>>> ','.join(my_list)
>>> '-'.join(my_list)
```

Another common way of converting a string into a list is with the string's `split()` method. This is useful for lightweight parsing of, for example, CSV (comma separated value) data.

```python
>>> my_string = "the,quick,brown,fox"
>>> my_string.split(",")
```


## Solutions

### Comprehensions

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = [num for num in range(0, 100) if num % 2 == 0]
>>> print(my_list)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

>>> import random
>>> my_dict = {num:random.randint(0, 100) for num in my_list}
>>> print(my_dict)
{0: 37, 2: 84, 4: 56, 6: 45, 8: 63, 10: 57, 12: 39, 14: 25, 16: 18, 18: 10, 20: 52, 22: 95, 24: 93, 26: 89, 28: 96, 30: 77, 32: 16, 34: 91, 36: 19, 38: 14, 40: 92, 42: 35, 44: 85, 46: 86, 48: 44, 50: 32, 52: 38, 54: 34, 56: 23, 58: 71, 60: 37, 62: 100, 64: 98, 66: 15, 68: 84, 70: 40, 72: 47, 74: 30, 76: 42, 78: 36, 80: 62, 82: 49, 84: 11, 86: 58, 88: 60, 90: 6, 92: 41, 94: 28, 96: 16, 98: 93}

>>> my_set = {num for num in my_dict.values()}
>>> print(my_set)
{6, 10, 11, 14, 15, 16, 18, 19, 23, 25, 28, 30, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 47, 49, 52, 56, 57, 58, 60, 62, 63, 71, 77, 84, 85, 86, 89, 91, 92, 93, 95, 96, 98, 100}
```

{{%/expand%}}

### Slicing

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = ["h", "e", "l", "l", "o", "!"]
>>> len(my_list)
6
>>> my_list[4:6]
['o', '!']
>>> my_list[4:]
['o', '!']
>>> my_list[-2:]
['o', '!']

```

```python
>>> my_list = [num for num in range(0, 100)]
>>> my_slice = my_list[30:70:2]
>>> print(my_slice)
[30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
>>> my_backwards_slice = my_slice[::-1]
>>> print(my_backwards_slice)
[68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30]
```

{{%/expand%}}


### `zip`

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> names = ["Nina", "Max", "Floyd", "Lloyd"]
>>> scores = [random.randint(0, 100) for name in names]
>>> scores
[41, 38, 96, 81]
>>> for name, score in zip(names, scores):
...     print(f"{name} got a score of {score}")
...
Nina got a score of 41
Max got a score of 38
Floyd got a score of 96
Lloyd got a score of 81
```

{{%/expand%}}

### Converting Between Types

#### Converting Between Numbers and Strings

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_string = str(100)
>>> my_string
'100'
>>> type(my_string)
<class 'str'>
>>> my_int = int(my_string)
>>> my_int
100
>>> type(my_int)
<class 'int'>
```

```python
>>> float("3.1415")
3.1415
```

```python
>>> int(3.1415)
3
```
{{%/expand%}}

#### Converting Between Lists and Strings

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = list("hello")
>>> my_list
['h', 'e', 'l', 'l', 'o']
>>> str(my_list)
"['h', 'e', 'l', 'l', 'o']"
```

```python
>>> ''.join(my_list)
'hello'

>>> ','.join(my_list)
'h,e,l,l,o'
>>> '-'.join(my_list)
'h-e-l-l-o'
```

```python
>>> my_string = "the,quick,brown,fox"
>>> my_string.split(",")
['the', 'quick', 'brown', 'fox']
```

{{%/expand%}}


