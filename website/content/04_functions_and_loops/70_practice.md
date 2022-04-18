+++
title = "Practice"
date = 2020-08-29T16:55:11-07:00
weight = 70
+++

## Functions

Let's try creating a basic function. Use tab to indent the second line, and press enter on an empty line to finish the function.

```python
>>> def add_numbers(x, y):
...     return x + y
... # Press Enter
```

Now let's try our new function. Type this into your REPL:

```python
>>> add_numbers(1, 2)
# Let's use the string formatting we learned in the last chapter
>>> print(f"The sum of 1 and 2 is {add_numbers(1, 2)}")
```

## The Importance of Whitespace

Here's an error that you'll become very familiar with during your career as a Pythonista, the `IndentationError`. Whitespace is important for defining function scope in python, so missing or extra indentations or spaces will cause the runtime to throw this error. Let's redefine our `add_numbers` function, but we'll forget to indent the second line, `return x + y`. Notice that the second line is directly under (at the same indentation level) as the `def`:

```python
>>> def add_numbers(x, y):
... return x + y
  File "<stdin>", line 2
    return x + y
         ^
IndentationError: expected an indented block
```

Notice how the runtime tells us the line that failed (`line 2`), gives you a copy of the line with an arrow pointing to the offending error (`return x + y`), and then tells you the error (`IndentationError`) with additional information (`expected an indented block`).

## Function Scope

As we saw earlier, scoping in Python happens with whitespace. Let's see this in action:

```python
>>> x = 1
>>> y = 2
>>> def add_numbers(x, y):
...     print(f"Inside the function, x = {x} and y = {y}")
...     return x + y
...
>>> print(f"Outside the function, x = {x} and y = {y}")
>>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
```

## Positional Arguments vs Keyword Arguments

The `x` and `y` arguments for our `add_numbers()` function are called positional arguments. Python also lets us declare *keyword* arguments. Keyword arguments are great for setting default values, because passing them is optional. Just remember that keyword arguments must come *after* any positional arguments. Let's make a more generic function for doing math:

```python
>>> def calculate_numbers(x, y, operation="add"):
...     if operation == "add":
...         return x + y
...     elif operation == "subtract":
...         return x - y
...
# Let's try our new function. Remember, if we don't pass the operation keyword argument, the default is "add"
>>> calculate_numbers(2, 3)
# You can pass a keyword argument as a normal positional argument
>>> calculate_numbers(2, 3, "subtract")
# You can also use the argument's keyword. This helps with readability
>>> calculate_numbers(2, 3, operation="subtract")
```

## Boolean Logic

### Comparisons

Let's practice using our comparison operators. Remember:

|Operator|Means|
|---|---|
|`<`|less-than|
|`<=`|less-than-or-equal-to|
|`>`|greater-than|
|`>=`|greater-than-or-equal-to|
|`==`|equals|
|`!=`|not-equals|

Remember, the first six operators test the object's *value*. `is` and `is not` test whether two objects are the same thing. This is useful for singletons, such as `None` or `False`. We won't be using them much in this intro course, but feel free to play with them.

```python
>>> 10 > 5
>>> 5 > 10
>>> 10 > 10
>>> 10 >= 10
>>> 5 < 10
>>> 5 < 5
>>> 5 <= 5
>>> 5 == 5
>>> 5 != 10
```

### Truthiness

Different languages have different ideas of what is "truthy" and "falsy." In Python, all objects can be tested for truth, and an object is considered True unless except under certain circumstances that we talked about earlier in the chapter. Remember that checking if an object is "equal" to another object doesn't necessarily mean the same thing. An object is considered "truthy" if it satisfies the check performed by `if` or `while` statements.

Let's try a few of these out:

```python
>>> 5 == True
>>> # The number 5 does not equal True, but...
>>> if 5:
...     print("The number 5 is truthy!")
...
>>> # The number 5 is truthy for an if test!
```

True and False can also be represented by 1 and 0
```python
>>> 1 == True
>>> 0 == False
```

### Boolean Operators

Python also supports boolean operators, although they're a little different than the comparison operators. Remember that `or` and `and` return one of their operands, rather than `True` or `False`.

|Operation|Result|
|---|---|
|`x or y`|`True` if either `x` or `y` is `True`|
|`x and y`|`True` if both `x` and `y` are `True`|
|`not x`|Negates the value of `x` (i.e. `True` if `x` is `False`)|

```python
# Of course, `and` and `or` aren't limited to two operands
>>> a = False
>>> b = False
>>> c = False
>>> a or b or c
>>> b = True
>>> a or b or c

>>> a and b and c
>>> a = True
>>> c = True
>>> a and b and c

>>> a = False
>>> b = False
>>> not a
>>> a and not b
```

## Control statements and looping

### `if`, `else`, and `elif`

Let's practice our branching statements. Remember that `elif` (short for `else if`) is an optional branch that will let you add another `if` test, and `else` is an optional branch that will catch anything not previously caught by `if` or `elif`.

```python
>>> def test_number(number):
...     if number < 100:
...         print("This is a pretty small number")
...     elif number == 100:
...         print("This number is alright")
...     else:
...         print("This number is huge!")
...
>>> test_number(5)
>>> test_number(99)
>>> test_number(100)
>>> test_number(8675309)
```

You can also have multiple conditions in an if statement. This function prints "Fizzbuzz!" if the number is divisible by both 3 and 5 (the `%` or modulo operator returns the remainder from the division of two numbers):

```python
>>> def fizzbuzz(number):
...     if number % 3 == 0 and number % 5 == 0:
...         print("Fizzbuzz!")
...
>>> fizzbuzz(3)
>>> fizzbuzz(5)
>>> fizzbuzz(15)
```

Let's also practice using `if` to test for an empty list. Remember that an empty list is "Falsey", or resolves to `False`. Write a function to print a list of elements, or an error message if the list is empty. Print a special message if a list item is `None`:

```python
>>> def my_func(my_list):
...     if my_list:
...         for item in my_list:
...             if item is None:
...                 print("Got None!")
...             else:
...                 print(item)
...     else:
...         print("Got an empty list!")
...
>>> my_func([1, 2, 3])
>>> my_func([2, None, "hello", 42])
>>> my_func([])
```


### The `for` loop, `range()` and `enumerate()`

Let's try making a list and looping over it:

```python
>>> my_list = [0, 1, 2]
>>> for num in my_list:
...     print(f"Next value: {num}")
...
```


If we're just interested in looping over a list of numbers, we can use the `range()` function instead. Remember that the first argument is inclusive and the second is exclusive:

```python
>>> for num in range(0, 3):
...     print(f"Next value: {num}")
...
```

Another useful function is `enumerate()`, which iterates over an iterable (like a list) and also gives you an automatic counter. `enumerate()` returns a tuple in the form of (`counter`, `item`).

```python
>>> my_list = ["foo", "bar", "baz"]
>>> for index, item in enumerate(my_list):
...     print(f"Item {index}: {item}")
...
```

We can also loop over a dictionary's keys and/or values. If you try to iterate over the dictionary object itself, what do you get?

```python
>>> my_dict = {"foo": "bar", "hello": "world"}
>>> for key in my_dict:
...     print(f"Key: {key}")
...
# This is equivalent to...
>>> for key in my_dict.keys():
...     print(f"Key: {key}")
...
```

The `keys()` method returns the dictionary's keys as a list, which you can then iterate over as you would any other list. This also works for `values()`

```python
>>> for value in my_dict.values():
...     print(f"Value: {value}")
...
```

The most useful function, however, is `items()`, which returns the dictionary's items as tuples in the form of (key, value):

```python
>>> for key, value in my_dict.items():
...     print(f"Item {key} = {value}")
...
```

### `return`

<!-- ## `break`, `continue`, and `return` -->

<!-- 
`break` and `continue` are important functions for controlling the program flow inside loops. `break` ends the loop immediately and continues executing from outside the loop's scope, and `continue` skips the remainder of the loop and continues executing from the next round of the loop. Let's practice:

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num == 3:
...         print("Found number 3!")
...         break
...     print("Not yet...")
...
```

Notice that "Not yet..." doesn't get printed for number 3, because we `break` out of the loop first. Let's try a `continue`:

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num < 3:
...         continue
...     elif num == 5:
...         print("Found number 5!")
...         break
...     print("Not yet...")
...
```

Notice that "Not yet..." doesn't get printed at all until the number is 3, because the `continue` short-circuits the loop back to the beginning. Then we `break` when we hit 5. -->

You can use the `return` keyword to break out of a loop within a function, while optionally returning a value.

```python
>>> def is_number_in_list(number_to_check, list_to_search):
...     for num in list_to_search:
...         print(f"Checking {num}...")
...         if num == number_to_check:
...             return True
...     return False
...
>>> my_list = [1, 2, 3, 4, 5]
>>> is_number_in_list(27, my_list)
>>> is_number_in_list(2, my_list)
```

Notice that our function `is_number_in_list` checks all the numbers in `my_list` on the first run, but on the next run, stops immediately when it hits 3 and returns `True`.

### `while` loop

Instead of looping over a sequence, `while` loops continue looping while a certain condition is met (or not met). The condition is checked at the beginning of every iteration.

```python
>>> counter = 0
>>> while counter < 3:
...     print(f"Counter = {counter}")
...     counter += 1
...
```

Notice that the loop ends once `counter` == 3, and the remainder of the loop is bypassed. You can also loop forever by using `while True` or `while False`, but you should make sure you have solid `break` conditions, or your program will just loop forever (unless that's what you want).

```python
>>> counter = 0
>>> while True:
...     print(f"Counter = {counter}")
...     if counter == 3:
...         break
...     counter += 1
...
```

### Nested Loops

Nesting loops is often necessary and sometimes tricky. The `break` keyword will only get you out of whichever loop you're `break`ing. The only way to exit all loops is with multiple `break` statements (at each level), or the `return` keyword (inside a function). For example:

```python
names = ["Rose", "Max", "Nina"]
target_letter = 'x'
found = False

for name in names:
    for char in name:
            if char == target_letter:
                    found = True
                    break

    if found:
        print(f"Found {name} with letter: {target_letter}")
        break
```

Or:

```python
>>> for x in range(0, 5):
...     for y in range(0, 5):
...         print(f"x = {x}, y = {y}")
...         if y == 2:
...             break
...
```

Notice how the inner `y` loop never gets above 2, whereas the outer `x` loop continues until the end of its range.


## Solutions


### Functions

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> add_numbers(1, 2)
3
# Let's use the string formatting we learned in the last chapter
>>> print(f"The sum of 1 and 2 is {add_numbers(1, 2)}")
The sum of 1 and 2 is 3
```

{{% /expand%}}


### Function Scope

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> x = 1
>>> y = 2
>>> def add_numbers(x, y):
...     print(f"Inside the function, x = {x} and y = {y}")
...     return x + y
...
>>> print(f"Outside the function, x = {x} and y = {y}")
Outside the function, x = 1 and y = 2
>>>
>>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
Inside the function, x = 5 and y = 6
The sum of 5 and 6 is 11
```

{{% /expand%}}


### Positional Arguments vs Keyword Arguments

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> def calculate_numbers(x, y, operation="add"):
...     if operation == "add":
...         return x + y
...     elif operation == "subtract":
...         return x - y
...
# Let's try our new function. Remember, if we don't pass the operation keyword argument, the default is "add"
>>> calculate_numbers(2, 3)
5
# You can pass a keyword argument as a normal positional argument
>>> calculate_numbers(2, 3, "subtract")
-1
# You can also use the argument's keyword. This helps with readability
>>> calculate_numbers(2, 3, operation="subtract")
-1
```

{{% /expand%}}

### Boolean Logic

#### Comparisons

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> 10 > 5
True
>>> 5 > 10
False
>>> 10 > 10
False
>>> 10 >= 10
True
>>> 5 < 10
True
>>> 5 < 5
False
>>> 5 <= 5
True
>>> 5 == 5
True
>>> 5 != 10
True
```

{{% /expand %}}

#### Truthiness

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> 5 == True
False
>>> # The number 5 does not equal True, but...
>>> if 5:
...     print("The number 5 is truthy!")
...
The number 5 is truthy!
>>> # The number 5 is truthy for an if test!
```

```python
>>> 1 == True
True
>>> 0 == False
True
```
{{% /expand %}}

#### Boolean Operators

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> a = False
>>> b = False
>>> c = False
>>> a or b or c
False
>>> b = True
>>> a or b or c
True

>>> a and b and c
False
>>> a = True
>>> c = True
>>> a and b and c
True

>>> a = False
>>> b = False
>>> not a
True
>>> a and not b
False
```

{{% /expand %}}


### Control statements and looping

#### `if`, `else`, and `elif`

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> def test_number(number):
...     if number < 100:
...         print("This is a pretty small number")
...     elif number == 100:
...         print("This number is alright")
...     else:
...         print("This number is huge!")
...
>>> test_number(5)
This is a pretty small number
>>> test_number(99)
This is a pretty small number
>>> test_number(100)
This number is alright
>>> test_number(8675309)
This number is huge!
```

```python
>>> def fizzbuzz(number):
...     if number % 3 == 0 and number % 5 == 0:
...         print("Fizzbuzz!")
...
>>> fizzbuzz(3)
>>> fizzbuzz(5)
>>> fizzbuzz(15)
Fizzbuzz!
```

```python
>>> def my_func(my_list):
...     if my_list:
...         for item in my_list:
...             if item is None:
...                 print("Got None!")
...             else:
...                 print(item)
...     else:
...         print("Got an empty list!")
...
>>> my_func([1, 2, 3])
1
2
3
>>> my_func([2, None, "hello", 42])
2
Got None!
hello
42
>>> my_func([])
Got an empty list!
```
{{%/expand%}}


#### The `for` loop, `range()` and `enumerate()`

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> my_list = [1, 2, 3]
>>> for num in my_list:
...     print(f"Next value: {num}")
...
Next value: 0
Next value: 1
Next value: 2
```

```python
>>> for num in range(0, 3):
...     print(f"Next value: {num}")
...
Next value: 0
Next value: 1
Next value: 2
```

```python
>>> my_list = ["foo", "bar", "baz"]
>>> for index, item in enumerate(my_list):
...     print(f"Item {index}: {item}")
...
Item 0: foo
Item 1: bar
Item 2: baz
```

```python
>>> my_dict = {"foo": "bar", "hello": "world"}
>>> for key in my_dict:
...     print(f"Key: {key}")
...
Key: foo
Key: hello

>>> for key in my_dict.keys():
...     print(f"Key: {key}")
...
Key: foo
Key: hello

>>> for value in my_dict.values():
...     print(f"Value: {value}")
...
Value: bar
Value: world

>>> for key, value in my_dict.items():
...     print(f"Item {key} = {value}")
...
Item foo = bar
Item hello = world
```

{{%/expand%}}

#### `return`

{{%expand "Here's what you should have seen in your REPL:" %}}
<!-- 
```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num == 3:
...         print("Found number 3!")
...         break
...     print("Not yet...")
...
Testing number 0
Not yet...
Testing number 1
Not yet...
Testing number 2
Not yet...
Testing number 3
Found number 3!
>>>
```

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num < 3:
...         continue
...     elif num == 5:
...         print("Found number 5!")
...         break
...     print("Not yet...")
...
Testing number 0
Testing number 1
Testing number 2
Testing number 3
Not yet...
Testing number 4
Not yet...
Testing number 5
Found number 5!
``` -->

```python
>>> def is_number_in_list(number_to_check, list_to_search):
...     for num in list_to_search:
...         print(f"Checking {num}...")
...         if num == number_to_check:
...             return True
...     return False
...
>>> is_number_in_list(27, my_list)
Checking 1...
Checking 2...
Checking 3...
Checking 4...
Checking 5...
False
>>> is_number_in_list(2, my_list)
Checking 1...
Checking 2...
True
```
{{%/expand%}}

#### `while` loop

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> counter = 0
>>> while counter < 3:
...     print(f"Counter = {counter}")
...     counter += 1
...
Counter = 0
Counter = 1
Counter = 2
```

```python
>>> counter = 0
>>> while True:
...     print(f"Counter = {counter}")
...     if counter == 3:
...         break
...     counter += 1
...
Counter = 0
Counter = 1
Counter = 2
Counter = 3
```

{{%/expand%}}

#### Nested Loops

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> for x in range(0, 5):
...     for y in range(0, 5):
...         print(f"x = {x}, y = {y}")
...         if y == 2:
...             break
...
x = 0, y = 0
x = 0, y = 1
x = 0, y = 2
x = 1, y = 0
x = 1, y = 1
x = 1, y = 2
x = 2, y = 0
x = 2, y = 1
x = 2, y = 2
x = 3, y = 0
x = 3, y = 1
x = 3, y = 2
x = 4, y = 0
x = 4, y = 1
x = 4, y = 2
```
{{%/expand%}}
