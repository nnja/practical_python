+++
title = "Practice"
date = 2020-08-29T16:59:55-07:00
weight = 60
+++


## `class`es and `self`

Let's practice making a simple class. Open a new file and save it as `class_example.py`, we'll be running this from the command line rather than the REPL. Pass in several variables and save them to the instance by using `self`:

```python
# class_example.py

class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

daily_driver = Vehicle("Subaru", "Crosstrek")
# By default, this is how python represents our object:
print(daily_driver)

# The variables we saved to the instance are available like this:
print(f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel}.")
```

## `class` Variables

We can also add     class variables - variables that exist for all instances of a class. Let's add a variable called `number_of_wheels` to the class scope:

```python
# class_example.py

class Vehicle:

    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel
```

Let's query both the instance and class variables. Note that we set the instance variable to 3, but the higher-level class variable is still set to 4.

```python
# class_example.py

daily_driver = Vehicle("Subaru", "Crosstrek")

daily_driver.number_of_wheels = 3

# Instance variables
print(f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel}.")
print(f"My {daily_driver.model} has {daily_driver.number_of_wheels} wheels.")

# Class variable
print(f"Most vehicles have {Vehicle.number_of_wheels} wheels.")
```

## Inheritance

Class inheritance in Python is super useful - you can easily create a hierarchy of classes to make your life easier and maximize code reuse. Let's subclass our `Vehicle` class and extend it by breaking out Cars and Trucks.

```python
# class_example.py

class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    number_of_wheels = 4


class Truck(Vehicle):

    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)
```

Note: we've moved the `number_of_wheels` variable to the subclasses. Our `Car` subclass sets this variable but instantiating a `Car` just passes through to `Vehicle.__init__()`. We do, however, provide a `__init__()` for `Truck`, which changes the default `fuel` to `diesel` and then calls `super().__init__()` which redirects to `Vehicle.__init__()`. This lets us make changes that are specific to `Truck` instances (but we can still call them `Vehicles`). Let's instantiate our subclasses:

```python
# class_example.py

daily_driver = Car("Subaru", "Crosstrek")
print(f"I drive a {daily_driver.make} {daily_driver.model}. "
      f"It uses {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels.")

truck = Truck("Ford", "F350")
print(f"I also have a {truck.make} {truck.model}. "
      f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels.")
```

## `type`, `isinstance`, and `issubclass`

The `type()` command tells us the type of an object - for example, a `Truck` or a `Car`. Note that it doesn't know anything about inheritance, so you can't use `type()` to check if a `Car` is a `Vehicle`. For that, we can use `isinstance()`. `issubclass()` is another useful function that we can use to see if a *class* (rather than an instance) is a subclass of another class. Add this to your code:

```python
# class_example.py

print(f"My daily driver is a {type(daily_driver)} and my truck is a {type(truck)}")

print(f"Is my daily driver a car? {isinstance(daily_driver, Car)}")
print(f"Is my truck a Vehicle? {isinstance(truck, Vehicle)}")
print(f"Is my truck a Car? {isinstance(truck, Car)}")

print(f"Is a Truck a subclass of Vehicle? {issubclass(Truck, Vehicle)}")
```

## Tracebacks and Exceptions

### Syntax Errors

Let's get more comfortable with exceptions. First, you've probably seen this one already: The `IndentationError`.

```python
>>> def my_function():
... print("Hello!")
  File "<stdin>", line 2
    print("Hello!")
        ^
IndentationError: expected an indented block
```

Notice that we started a new function scope with the `def` keyword, but didn't indent the next line of the function, the `print()` argument.

You've probably also seen the more general `SyntaxError`. This one's probably obvious - something is misspelled, or the syntax is otherwise wrong. Python gives us a helpful little caret `^` under the earliest point where the error was detected, however you'll have to learn to read this with a critical eye as sometimes the actual mistake precedes the invalid syntax. For example:

```python
>>> a = [4,
... x = 5
  File "<stdin>", line 2
    x = 5
      ^
SyntaxError: invalid syntax
```

Here, the invalid syntax is `x = 5`, because assignment statements aren't valid list elements, however the actual error is the missing right bracket `]` on the line above.

### Common Exceptions

You'll get plenty of practice triggering syntax errors on your own. Let's practice triggering some exceptions. Type this *perfectly valid* code into your REPL and see what happens:

```python
>>> a = 1 / 0
```

Of course, you'll get a divide-by-zero error, or as Python calls it, `ZeroDivisionError`. Some other common errors are `TypeError` when trying to perform an action on two unrelated types, `KeyError` when trying to access a dictionary key that doesn't exist, and `AttributeError` when trying to access a variable or call a function that doesn't exist on an object.

```python
>>> 2 + "3"

>>> my_dict = {"hello": "world"}
>>> my_dict["foo"]

>>> my_dict.append("foo")
```


### Raising our own Exceptions

Making our own Exceptions is cheap and easy, and useful for keeping track of various error states that are specific to your application. Simply inherit from the general `Exception` class:

```python
>>> class MyException(Exception):
...     pass
...
>>> raise MyException()
```

It's also sometimes helpful to change the default behavior for your custom Exceptions. In this case, you can simply provide your own `__init__()` method inside your Exception subclass:


```python
>>> class MyException(Exception):
...     def __init__(self, message):
...             new_message = f"!!!ERROR!!! {message}"
...             super().__init__(new_message)
...
>>> raise MyException("Something went wrong!")
```

### `try`, `except`

In Python, the "try-catch" statements use `try` and `except`. As we discussed, `try` is the code that could possibly throw an Exception, and `except` is the code that runs if the error is raised. Practice catching a `KeyError` by `try`ing to access a fake dictionary key:

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError:
...     print("Oh no! That key doesn't exist")
...
```

Let's add in catching the specific `KeyError` object so that we can access it during the `except` block:

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError as key_error:
...     print(f"Oh no! The key {key_error} doesn't exist!")
...
```


### Re-Raising

Sometimes it's helpful to catch an error, perform an action, and then pass the error on rather than swallowing it. This is useful when, for example, something goes wrong deep inside your code and you need to perform a special action, but also let code further up the chain know that something is wrong and the program can't continue. Let's divide one number by other, decrementing until we hit zero. Catch that error and immediately raise a `RuntimeError`:

```python
>>> while True:
...     for divisor in range(5, -1, -1):
...         try:
...             quotient = 10 / divisor
...             print(f"10 / {divisor} = {quotient}")
...         except ZeroDivisionError:
...             print("Oops! We tried to divide by zero!")
...             raise RuntimeError
...
```

## Solutions

### `class`es and `self`

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python class_example.py
<__main__.Vehicle object at 0x10555c780>
I drive a Subaru Crosstrek. It runs on gas.
```

{{% /expand%}}

### `class` Variables

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python class_example.py
I drive a Subaru Crosstrek. It runs on gas.
My Crosstrek has 3 wheels.
Most vehicles have 4 wheels.
```

{{% /expand%}}

### Inheritance

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python class_example.py
I drive a Subaru Crosstrek. It uses gas and has 4 wheels.
I also have a Ford F350. It uses diesel and has 6 wheels.
```

{{% /expand%}}

### `type`, `isinstance`, and `issubclass`

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python class_example.py
My daily driver is a <class '__main__.Car'> and my truck is a <class '__main__.Truck'>
Is my daily driver a car? True
Is my truck a Vehicle? True
Is my truck a Car? False
Is a Truck a subclass of Vehicle? True
```

{{% /expand%}}

### Tracebacks and Exceptions

#### Common Exceptions

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> a = 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

```python
>>> 2 + "3"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> my_dict = {"hello": "world"}
>>> my_dict["foo"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'

>>> my_dict.append("foo")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'
```
{{% /expand%}}

#### Raising our own Exceptions

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> class MyException(Exception):
...     pass
...
>>> raise MyException()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyException
```

```python
class MyException(Exception):
...     def __init__(self, message):
...         new_message = f"!!!ERROR!!! {message}"
...         super().__init__(new_message)
...
>>> raise MyException("Something went wrong!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyException: !!!ERROR!!! Something went wrong!
```
{{% /expand%}}

#### `try`, `except`

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError:
...     print("Oh no! That key doesn't exist")
...
Oh no! That key doesn't exist
```

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError as key_error:
...     print(f"Oh no! The key {key_error} doesn't exist!")
...
Oh no! The key 'foo' doesn't exist!
```
{{% /expand%}}

#### Re-Raising

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> while True:
...     for divisor in range(5, -1, -1):
...         try:
...             quotient = 10 / divisor
...             print(f"10 / {divisor} = {quotient}")
...         except ZeroDivisionError:
...             print("Oops! We tried to divide by zero!")
...             raise RuntimeError
...
10 / 5 = 2.0
10 / 4 = 2.5
10 / 3 = 3.3333333333333335
10 / 2 = 5.0
10 / 1 = 10.0
Oops! We tried to divide by zero!
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
RuntimeError
```

What happened here? We got two exceptions! First, our code hit the `ZeroDivisionError`, which we caught, and printed our "Oops!" message. Then, the interpreter saw that we raised a `RuntimeError`, which we didn't catch, so it broke us out of our `while True` loop and ended the program with a Traceback.

{{% /expand%}}
