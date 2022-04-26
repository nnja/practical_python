+++
title = "Exceptions"
date = 2020-08-29T17:00:45-07:00
weight = 50
+++

## All About Exceptions

Built-in exceptions and easy exception handling is one of the shining features of Python. Technically, errors that happen during parsing are called `SyntaxError`s - these will probably be the most common errors you see, and usually happen because of a mistake in whitespace, a syntax misunderstanding, or a simple typo.

Even if the syntax is correct, errors can still occur when your program is run. We call these Exceptions, and there are many different types (this is a good thing, because the more specifically we know what went wrong, the better we can handle it).

An un-handled exception is fatal: it will print debugging information (called a traceback), stop the interpreter, and exit your program. However, once you learn to handle Exceptions, you can cover your bases and write programs that are robust in the face of issues.


## Types of Exceptions

Python has many useful built-in exceptions that you'll probably encounter in your travels. Some of the more common ones that you'll run into are:

|Exception|Cause of Error|
|---|---|
|AttributeError|Raised when an attribute assignment or reference fails.|
|ImportError|Raised when the imported module is not found.|
|IndexError|Raised when the index of a sequence is out of range.|
|KeyError|Raised when a key is not found in a dictionary.|
|KeyboardInterrupt|Raised when the user hits interrupt key (Ctrl+c or delete).|
|NameError|Raised when a variable is not found in local or global scope.|
|SyntaxError|Raised by parser when a syntax error is encountered.|
|IndentationError|Raised when there is incorrect indentation.|
|ValueError|Raised when a function gets an argument of correct type but improper value.|

You can find a more detailed list of built-in exceptions in the [Python documentation](https://docs.python.org/3/library/exceptions.html).

## Exiting your Program

As we mentioned, exceptions that are allowed to bubble up to the top level (called *unhandled* exceptions) will cause your program to exit. This is generally unwanted - even if an error is unrecoverable, we still want to provide more detailed information about the error for later inspection, or a pretty error for the user if our program is user-facing, and in most cases, we want the program to go back to doing what it was doing.

What if we want our program to stop, though? You may already be familiar with `Ctrl-c`, the age-old posix method of sending SIGINT (an interrupt signal) to a program. You may be surprised to know that asking your operating system to send SIGINT to Python causes, yes, an exception - `KeyboardInterrupt`. And yes, you can catch `KeyboardInterrupt`, but this will make your program a little harder to kill.

You can also use `sys.exit()` from the built-in `sys` library. It's generally not a good idea to pepper `sys.exit()` around your code, as it makes it harder to control when your program exits, but this can be a handy function for controlling how and when your program exits. By default, `sys.exit()` with no parameters will exit with a `0` return code, which, by posix convention, signals success. You can pass an integer to `sys.exit()` if you'd like to exit with a non-zero return code (usually signaling some sort of failure condition). You can also pass a string to `sys.exit()`, which will get printed to the command line, along with a return code of `1`.

`sys.exit()` generates a `SystemExit` exception, which inherits from the master `BaseException` class, which makes it possible for clean-up handlers (such as `finally` statements) to run.

## Try, Except

Many languages have the concept of the "Try-Catch" block. Python uses four keywords: `try`, `except`, `else`, and `finally`. Code that can possibly throw an exception goes in the `try` block. `except` gets the code that runs if an exception is raised. `else` is an optional block that runs if no exception was raised in the `try` block, and `finally` is an optional block of code that will run last, regardless of if an exception was raised. We'll focus on `try` and `except` for this chapter.

A basic example looks like this:

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That number was invalid")
```

First, the `try` clause is executed. If no exception occurs, the `except` clause is skipped and execution of the `try` statement is finished. If an exception occurs in the `try` clause, the rest of the clause is skipped. If the exception's type matches the exception named after the `except` keyword, then the `except` clause is executed. If the exception doesn't match, then the exception is *unhandled* and execution stops.


### The `except` Clause

An `except` clause may have multiple exceptions, given as a parenthesized tuple:

```python
try:
    # Code to try

except (RuntimeError, TypeError, NameError):
    # Code to run if one of these exceptions is hit
```

A `try` statement can also have more than one `except` clause:

```python
try:
    # Code to try

except RuntimeError:
    # Code to run if there's a RuntimeError

except TypeError:
    # Code to run if there's a TypeError

except NameError:
    # Code to run if there's a NameError
```

### Finally

Finally, we have `finally`. `finally` is an optional block that runs after `try`, `except`, and `else`, regardless of if an exception is thrown or not. This is good for doing any cleanup that you want to happen, whether or not an exception is thrown.

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print("Goodbye!")
...
Goodbye!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

As you can see, our Goodbye! gets printed just before the unhandled `KeyboardInterrupt` gets propagated up and triggers the traceback.

## Exception Hierarchy

Python has many useful built-in exceptions that you'll probably encounter in your travels. You can find a detailed list of built-in exceptions in the [Python documentation](https://docs.python.org/3/library/exceptions.html).

An important thing to know is that exceptions, like everything else in Python, are just objects. They follow an inheritance hierarchy, just like classes do. For example, the `ZeroDivisionError` is a subclass of `ArithmeticError`, which is a subclass of `Exception`, itself a subclass of `BaseException`.

```python
>>> issubclass(ZeroDivisionError, ArithmeticError)
True
>>> issubclass(ArithmeticError, Exception)
True
>>> issubclass(Exception, BaseException)
True

# Thus,
>>> issubclass(ZeroDivisionError, BaseException)
True
```

So, if you wanted to catch a divide-by-zero error, you could use `except ZeroDivisionError`. But you could also use `except ArithmeticError`, which would catch not only `ZeroDivisionEror`, but also `OverflowError` and `FloatingPointError`. You could use `except Exception`, but this is not a good idea, as it will catch almost *every* type of error, even ones you weren't expecting. We'll discuss this a bit later.

A full chart of the hierarchy for built-in exceptions can be found at the bottom of the [Python documentation](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).

## Best Practices

### Catch More Specific Exceptions First

Remember, your `except` handlers are evaluated in order, so be sure to put more specific exceptions first. For example:

```python
>>> try:
...     my_value = 3.14 / 0
... except ArithmeticError:
...     print("We had a general math error")
... except ZeroDivisionEror:
...     print("We had a divide-by-zero error")
...
We had a general math error
```

When we tried to divide by zero, we inadvertently raised a ZeroDivisionError. However, because ZeroDivisionError is a subclass of ArithmeticError, and `except ArithemticError` came first, the information about our specific error was swallowed by the `except ArithemticError` handler, and we lost more detailed information about our error.

### Don't Catch `Exception`

It's bad form to catch the general `Exception` class. This will catch every type of exception that subclasses the `Exception` class, which is almost all of them. You may have errors that you don't care about, and don't affect the operation of your program, or maybe you're dealing with a flaky API and want to swallow errors and retry. By catching `Exception`, you run the risk of hitting an unexpected exception that your program actually can't recover from, or worse, swallowing an important exception without properly logging it - a huge headache when trying to debug programs that are failing in weird ways.


### Definitely don't catch `BaseException`

Catching `BaseException` is a really bad idea, because you'll swallow every type of Exception, including `KeyboardInterrupt`, the exception that causes your program to exit when you send a SIGINT (Ctrl-C). Don't do it.

## Custom Exceptions


As we mentioned, exceptions are just regular classes that inherit from the `Exception` class. This makes it super easy to create our own custom exceptions, which can make our programs easier to follow and more readable. An exception need not be complicated, just inherit from `Exception`:

```python
>>> class MyCustomException(Exception):
...     pass
...
>>> raise MyCustomException()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

It's OK to have a custom `Exception` subclass that only `pass`-es - your exception doesn't need to do anything fancy to be useful. Having custom exceptions - tailored to your specific use cases and that you can raise and catch in specific circumstances - can make your code much more readable and robust, and reduce the amount of code you write later to try and figure out what exactly went wrong.

Of course, you can get as fancy as you want. You can send additional information, like messages, to your exceptions. Just add an `__init__()` method to your exception class, with whatever arguments you want.

```python
class IncorrectValueError(Exception):
...     def __init__(self, value):
...         message = f"Got an incorrect value of {value}"
...         super().__init__(message)
...
>>> my_value = 9999
>>> if my_value > 100:
...     raise IncorrectValueError(my_value)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
__main__.IncorrectValueError: Got an incorrect value of 9999
```

`Exception` takes an optional string argument message that gets printed with your exception. We pass our erroneous value to our `IncorrectValueError` object, which constructs a special message and passes it its parent class, `Exception`, via `super().__init__()`. The custom message string, along with the value for context, gets printed along with our error traceback.

### A Custom Exception for our GitHub API app

If we wanted to write a custom Exception for our GitHub API app from earlier, it might look something like this.

```python
class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)
```

Notice how it takes the HTTP status code into account, and displays a custom error message for the 403 Rate Limited Reached status code.
