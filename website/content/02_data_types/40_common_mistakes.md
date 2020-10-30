+++
title = "Common Mistakes"
date = 2020-08-29T16:53:27-07:00
weight = 40
+++

There are a few common errors and exceptions that you'll encounter when working with strings and numbers.

## `str`ings

### Problem: Mismatched string quotes

{{% notice info %}}
Mismatched string quotes will result in a `SyntaxError`
{{% /notice %}}

When we try to start a String with one type of quote, and end with another, we'll see a syntax error.

```python
>>> name = 'Hello"
  File "<stdin>", line 1
    name = "Hello'
                 ^
SyntaxError: EOL while scanning string literal
```

**Solution:** use matching quote types for defining your strings. Either single quotes `'Hello'` or double quotes `"Hello"`.

### Problem: Trying to print a String and a number with concatenation using the "+" symbol.

{{% notice info %}}
Trying to add or concatenate a String and a number will result in a `TypeError`
{{% /notice %}}

If you add try to add (or concatenate) a String and a number, you'll get an error saying that adding the two types together isn't possible.

```python
>>> print(3 + " Three")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Solutions:**

There are two possible solutions here, for two different scenarios.

#### Converting Types to Strings

In the first scenario, you'd like to add a number to a string via concatenation. In order to do that, you must first convert the number to a string via the `str()` method. This isn't so useful while we work in the REPL, but will become useful when we start running Python programs. 

```python
>>> my_num = 3
>>> print(str(my_num) + " Three")
3 Three
```

In the second scenario, you'd like to a convert a number that's contained in a string (ex: `"3"`) into an Integer, so you can use it like any other number. In this case, you'd like to convert it to an Integer, with the `int()` method.

```python
>>> str_num = "3"
>>> print(int(str_num) + 5)
8
```

## `list`s

### Problem: Forgetting commas between items

{{% notice info %}}
If you forget to include commas between your items, you'll get a `SyntaxError`.
{{% /notice %}}

```python
>>> numbers = [1, 2 3]
  File "<stdin>", line 1
    numbers = [1, 2 3]
                    ^
SyntaxError: invalid syntax
```

The REPL makes it difficult to forget the closing bracket, but if you forget it while writing code in a Python file, you'll see a `SyntaxError` with a different name. It'll say: `SyntaxError: unexpected EOF while parsing` or `SyntaxError: invalid syntax`.

For example:

```python
# Python file: program.py
names = ["Nina",
x = 5
```

```bash
# In a shell
(env) $ python program.py
  File "/Users/nina/Desktop/program.py", line 2
    x = 5
      ^
SyntaxError: invalid syntax
```

Notice how the `SyntaxError` points to a completely valid line of Python code. In these cases, you also need to check the line of code **before** the line with the `SyntaxError`. There, we'll notice that we forgot the closing bracket of our `names` list.

## Indentation

Indentation is important in Python. If you have extra whitespace in your code, you may see an `IndentationError`.

```python
>>>   a = 5
  File "<stdin>", line 1
    a = 5
IndentationError: unexpected indent
```

**Solution:**

 Remove the extra whitespace and try again. 