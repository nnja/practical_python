+++
title = "Modules and Imports"
date = 2020-08-29T17:01:18-07:00
weight = 50
+++


## Standard Library

Python has always had a "batteries included" philosophy - having a rich and versatile standard library which is immediately available, without making the user download separate packages. This is thought to have contributed to Python's early success. No matter what you're trying to accomplish, there's probably a built-in library that can help you do what you want.

The downside to this is that the standard libraries need to maintain backwards compatibility. Some were quick hacks, hard to use, poorly designed and now impossible to fix, or have simply been rendered obsolete. Luckily, Python also makes it easy to install and use external libraries - we'll cover this later.


### The Standard Library

There are some great libraries included with Python that you'll probably end up seeing or using frequently. `sys` provides system-specific parameters and functions, such as `exit()`. `os` has miscellaneous operating system interfaces, and provides the excellent `os.path` submodule for handling file paths on any operating system. `math` gives you all the advanced math function. `json` is an easy-to-use json parser and encoder. Python even gives you built-in libraries for database access, logging, internet protocols, multimedia, debugging, and even libraries for extending Python itself. The full list of standard libraries can be found in the [Python documentation](https://docs.python.org/3/library/).

As a quick example, let's look at Python's `datetime` library. You can easily make a `datetime` object that represents any given point in time. For example:

```python
>>> import datetime
>>> right_now = datetime.datetime.now()
>>> print(right_now)
2020-10-29 23:29:53.798740
>>> repr(right_now)
'datetime.datetime(2020, 10, 29, 23, 29, 53, 798740)'
```

We can even make a `datetime` object for an arbitrary date, and subtract it from right now to get a `timedelta` object:

```python
>>> new_years = datetime.datetime(2020, 1, 1, 0, 0)
>>> print(new_years)
2019-01-01 00:00:00
>>> delta = right_now - new_years
>>> print(delta)
302 days, 23:29:53.798740
```

We can easily see that it's been over 302 days from `new_years` until `right_now`. We'll come back to `datetime` later in this chapter.

## Modules and Imports


Python has a simple package structure. Any directory with a file named `__init__.py` can be considered a Python module.

{{% notice info %}}
Note: a `__init__.py` file is no longer *required* for Python 3 modules, but it's still supported and can be useful.
{{% /notice %}}

For example, let's make a basic function and start a new module to house it:

```python
def add_numbers(x, y):
    return x + y
```

Let's put our function in a file called `__init__.py` and place it in a folder called `my_math_functions`. Now, as long as the folder `my_math_functions` is somewhere in our `PYTHONPATH`, we can `import my_math_functions` and reach `add_numbers()`. If we start our REPL from the folder that contains `my_math_functions`, we can import it:

```python
>>> import my_math_functions
>>> my_math_functions.add_numbers(1, 2)
3
```

### Best Practices

There a few different ways to import modules or even just specific objects from modules. You can import *everything* from a module into the local namespace using `*`:

```python
>>> from my_math_functions import *
>>> add_numbers(1, 2)
3
```

This isn't a good practice, because it's hard to tell where a specific function is coming from without the namespace context. Also, function names can conflict, and this can make things very difficult to debug.

It is better to import functions specifically:

```python
>>> from my_math_functions import add_numbers
>>> add_numbers(1, 2)
3
```

This make things a little clearer, as we can look at the top and see where the `add_number()` function came from. However, an even better way is to just import the module and use it in calls to maintain the namespace context:

```python
>>> import my_math_functions
>>> my_math_functions.add_numbers(1, 2)
3
```

This can be slightly more verbose, but unless it makes your function calls ridiculously long, it generally makes things much easier to debug.

{{% notice tip %}}
You can use the `as` keyword to make things a little easier on yourself.
{{% /notice %}}

```python
>>> import my_math_functions as mmf
>>> mmf.add_numbers(1, 2)
3
```

### PYTHONPATH

What is the `PYTHONPATH` we mentioned earlier? This is a list of paths on your system where Python will look for packages. Python will always look first in the working directory (the folder you're in when you start the REPL or run your program), so if your module folder is there, you can import it. You can also install your modules just like any other external modules, using a `setup.py` file. It's also possible to change or add paths to your `PYTHONPATH` list if you need to store modules elsewhere, but this isn't a very portable solution.

