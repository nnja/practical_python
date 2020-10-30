+++
title = "Numbers"
date = 2020-08-29T16:53:14-07:00
weight = 10
+++

There are three different types of numbers in Python: `int` (integer), `float`, and `complex`.

```python
# These are all integers
>>> x = 4
>>> y = -193394
>>> z = 0
```

```python
# These are all floats
>>> x = 5.0
>>> y = -3983.2
>>> z = 0.
```

```python
# This is a complex number
>>> x = 42j
>>> type(x)
<class 'complex'>
```

In Python, integers and other simple data types are just objects under the hood. That means that you can create new ones by calling methods. You can provide either a number or a string.

You'll rarely use this syntax to declare variables in code, but you'll need to remember it to switch your variable between different types.

```python
>>> x = int(4)
>>> z = float(5.0)
```

To create a new integer from a string input, call `int()`:

```python
>>> y = int('4')
>>> y
4
>>> type(y)
<class 'int'>
```

Python also provides a `decimal` library, which has certain benefits over the `float` datatype. For more information, refer to the [Python documentation](https://docs.python.org/3/library/decimal.html).

## Mathematical Operations

Common mathematical operations can be performed on numbers in Python.

```python
>>> 5 + 4
9
>>> 10 - 7
3
>>> a = 3
>>> b = 2
>>> a * b  # multiplication
6
>>> a ** b  # pow -- 3^2
9
>>> 5.0 / 2.0
2.5
>>> # Use parenthesis to guarantee order
>>> (2 + 2) * (3 + 5)
32
```

Know that:
- If you add a `float` and an `int`, the resulting type will be a `float`.
- If you divide two `int`s (integers), the result will be of type `float`, unless you use the special integer division operator (`//`)

```python
>>> 3.0 + 1
4.0
>>> 6 / 3
2.0
>>> 6 // 3
2
```

Python also has several handy built-in methods for working with numbers, like `min()` for minimum, `max()` for maximum, and `round()` for rounding to the nearest integer. 

```python
>>> min(3, 1, 2)
1
>>> max(100, 0, 5)
100
>>> round(3.1)
3
>>> round(5.9)
6
```

If you need more advanced methods, Python also offers a [`math` module](https://docs.python.org/3/library/math.html) in the standard library.

## Boolean Types

In Python, Booleans are of type `bool`. Surprisingly, the boolean types `True` and `False` are also numbers under the hood.

* `True` is `1` under the hood.
* `False` is `0` under the hood.

```python
>>> True == 1
True
>>> False == 0
True
```

That means you can do silly things, like add two Boolean numbers together.