+++
title = "Strings"
date = 2020-08-29T16:53:20-07:00
weight = 20
+++

### Representing Strings

Strings in Python can be enclosed either with single quotes like `'hello'` or double quotes, like `"hello"`.

To use the same type of quote within a string, that quote needs to be **escaped** with a `\` - backwards slash.

```python
greeting = 'Hello, it\'s Nina'
```

Alternately, mixed quotes can be present in a Python string without escaping.

```python
# Notice that the single quote ' is surrounded by
# double quotes, ""
greeting = "Hello, it's Nina"
```

Long multi-line strings can be represented in between `"""` (triple quotes), but the whitespace will be part of the string.

```python
long_greeting = """
                Greetings and salutations, dear Nina.
                I'm superfluous with my words,
                and require more space to say Hello!"
                """
```

### String Values

Python offers two methods of seeing what's inside a string -- `print()` and `repr()`. You can differentiate between the two by their purpose. 

Use `print()` when you want to display readable output to end users. Use `repr()` to display unambiguous output to developers, like for debugging purposes.

For now, we'll focus on `print()` and come back to `repr()` later in the day when we talk about classes in object-oriented Python.

#### `print()`

Strings can be printed out using the `print()` function in Python. While you're working the REPL, you'll see that variables are displayed for you. When you move on to writing standalone Python programs, that will no longer be the case.

To use the `print()` function, call it with a regular or formatted string.

```python
>>> print("Hello")
Hello
>>> name = "Nina"
>>> print(name)
Nina
```

A quick way to print the value of multiple variables without formatting them is to pass them into the `print()` method as comma-separated values. This will print the value of each variable separated by a space.

```python
>>> print("October is month", 10)
October is month 10
```


### String Formatting

#### Concatenation

Strings can also be **concatenated** (added together) using the `+` operator to combine an arbitrary number of Strings. For example:

```python
salutation = "Hello "
name = "Nina"
greeting = salutation + name
# The value of greeting will be "Hello Nina"
```
Generally, you'll want to avoid concatenating more than a handful of strings in production code because it's inefficient. Use string formatting instead.

#### f-strings

There are several types of string formatting in Python, but f-strings introduced in Python 3.7 are the most modern and efficient. 

f-strings start with the letter `f`. Variables and expressions can be inserted into the string by enclosing them in curly brackets.

You don't need to convert variables to strings when using f-string formatting. It happens under the hood.

```python
>>> name = "Nina"
>>> greeting = f"Hello, {name}"

>>> print(greeting)
Hello, Nina
```

#### Trimming a string

Python strings have some very useful functions for trimming whitespace. `strip()` returns a new string after removing any leading and trailing whitespace. `rstrip()` does the same but only removes trailing whitespace, and `lstrip()` only trims leading whitespace.

```python
>>> my_string = "   Hello World!   "
>>> print(f">{my_string.strip()}<")
>Hello World!<
```

These functions also accept an optional argument of characters to remove. Let's remove all leading or trailing commas, an operation that's useful when working with `csv` files for example:

```python
>>> my_string = "Hello World!,,,"
>>> print(my_string.strip(","))
Hello World!
```

#### Replacing Characters

Strings have a useful function for replacing characters - just call `replace()` on any string and pass in what you want replace, and what you want to replace it with:

```python
>>> my_string = "Hello, world!"
>>> my_string.replace("world", "Nina")
'Hello, Nina!'
```

#### Working with strings

Remember, you don't need to memorize every method for working with strings.

Instead, just call `dir()` on `str` in the REPL to see all the string methods available, and call `help()` on any method to see helpful docs on what that method does and what arguments it accepts.

```python
>>> dir(str)
>>> help(str.title)
Help on method_descriptor:

title(self, /)
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.
```

### `str.format()` and `%` formatting

Python has two older methods for string formatting that you'll probably come across at some point. `str.format()` is the more verbose older cousin to `f-strings` - variables appear in brackets in the string, and must be passed in to the `format()` call. For example:

```python
>>> name = "Nina"
>>> print("Hello, my name is {name}".format(name=name))
Hello, my name is Nina
```

Note that the variable name inside the string is local to the string - it must be assigned to an outside variable inside the `format()` call, hence `.format(name=name)`.

%-formatting is a much older method of string interpolating and isn't used much anymore. It's very similar to the methods used in C/C++. Here, we'll use `%s` as our placeholder for a string, and pass the `name` variable in to the formatter by placing it after the `%` symbol.

```python
>>> name = "Nina"
>>> print("Hello, my name is %s" % name)
Hello, my name is Nina
```

For formatting strings in modern Python, reach for f-strings instead.