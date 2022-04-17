+++
title = "Boolean Logic"
date = 2020-08-29T16:56:10-07:00
weight = 30
+++

## Truthiness

Evaluating expressions to be `True` or `False` will help us control the flow of our program.

### cheat sheet

| type                                        	| truthiness                                                                     	|   	|
|---------------------------------------------	|--------------------------------------------------------------------------------	|---	|
| `int`                                       	| `0` is `False`, all other numbers are `True` (including negative)              	|   	|
| containers - `list`, `tuple`, `set`, `dict` 	| empty containers evaluate to `False`, containers with items evaluate to `True`) 	|   	|
| `None`                                      	| `False`                                                                        	|   	|

We talked about `boolean` types (`True` and `False`) earlier. `True` and `False` are keywords in Python, so make sure you don't name your variables the same thing.

```python
>>> True
True
>>> False
False
```

Sometimes the truth is obvious. For example `3 < 5` is always `True`. Other times, in Python, the truth value might surprise you. Let's review. First, let's start with an expression we know is always `True`.

```python
>>> 3 < 5
True
```

{{% notice tip %}}
Tip: If you want to test your assumptions about an expression that returns `True` or `False`, you can pass it into the constructor for `bool`eans: `bool(expression)`.
{{% /notice %}}

### Numbers

In Python, the integer `0` is always `False`, while every other number, *including negative numbers*, are `True`. In fact, under the hood, `bool`eans inherit from `int`egers.

```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
```

### Sequences

Empty sequences in Python always evaluate to `False`, **including empty `str`ings.**

```python
>>> bool("")    # String
False
>>> bool([])    # Empty List
False
>>> bool(set()) # Empty Set
False
>>> bool({})    # Empty Dictionary
False
>>> bool(())    # Empty Tuple
False
```

Sequences with at least one value will evaluate to `True`.

```python
>>> bool("Hello")   # String
True
>>> bool([1])       # List
True
>>> bool({1})       # Set
True
>>> bool({1: 1})    # Dictionary
True
>>> bool((1,))      # Tuple
True
```

### `None`

The `None` type in Python represents nothing. No returned value. It shouldn't come as a surprise that the truthiness of `None` is `False`.

```python
>>> bool(None)
False
```

`None` is commonly used as a placeholder to mean *"I haven't set this value yet."* Since empty `str`ings and sequences evaluate to `False`, we need to be very careful when we're checking if a sequence has been *declared* or not, or if it's *empty*.   We'll review this concept again when talking about `if` statements later in the day.

```python
>>> my_name = None
>>> bool(my_name)
False
>>> my_name = ""
>>> bool(my_name)
False

>>> my_list = None
>>> bool(my_list)
False
>>> my_list = []
>>> bool(my_list)
False
```

## Comparisons

How can we compare different values with each other?

### Order Comparisons Cheat Sheet

|Operator|Means|
|---|---|
|`<`|less-than|
|`<=`|less-than-or-equal-to|
|`>`|greater-than|
|`>=`|greater-than-or-equal-to|

In Python, comparing numbers is pretty straight forward.

```python
>>> 1 < 10  # 1 is less than 10? True
True
>>> 20 <= 20  # 20 is less than or equal to 20? True
True
>>> 10 > 1  # 10 is greater than 1? True
True
>>> -1 > 1  # -1 is greater than 1? False
False
>>> 30 >= 30  # 30 is greater than or equal to 30? True
True
```

Things get interesting when you try to compare strings. Strings are compared lexicographically. That means by the ASCII value of the character. You don't need to know much about ASCII, besides that capital letters come before lower case ones.

Each character in the two strings is checked one by one, until a character is found that is of a different value. That determines the order. Under the hood, this allows Python to sort strings by comparing them to each other.

```python
>>> "T" < "t"  # Upper case letters are "lower" valued.
True
>>> "a" < "b"
True
>>> "bat" < "cat"
True
```

### Equality Cheat Sheet

|Operator|Means|
|---|---|
|`==`|equals|
|`!=`|not-equals|

The equality operators `val1 == val2` *(`val1` equals `val2`)* and `val1 != val2` *(`val1` doesn't equal `val2`)* compare the contents of two different values and return a `bool`ean.

Equality works like you'd expect it to for simple data types.

```python
>>> a = 1
>>> b = 1
>>> a == b
True
>>> a != b
False

>>> a = "Nina"
>>> b = "Nina"
>>> a == b
True
>>> a != b
False
```

Equality for container types is interesting. Even though `a` and `b` are two different `list`s, their contents are still the same. So compared two lists containing the same values with `==` will return `True`.

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a != b
False
```

### Identity Cheat Sheet

|Operator|Means|
|---|---|
|`is`| *is* the same object in memory? (not equality!)|
|`is not`| *is not* the same object in memory? (not equality!)|

The `is` keywords tests if the two compared objects are stored in the same memory location. I won't go into too much detail into why, but remember **not** to use `is` when what you actually want to check for is equality.

{{% notice note %}}
This is something that trips up Python beginners, so make sure you remember that *equality* (`==`, `!=`) **is not** the same as *identity* (`is`, `not is`).
{{% /notice %}}


```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]

>>> a == b  # Testing for equality. a and b contain the same values
True
>>> a is b  # Testing for identity. a and b are NOT the same object.
False
```

{{% notice tip %}}
When you're first starting out, the only place you'll want to use the `is` keyword is to explicitly compare a value to the built-in types of `None`, `True`, or `False`.
{{% /notice %}}

```python
>>> a = True
>>> a is True
True

>>> b = False
>>> b is False
True
>>> b is not True   # Opposite of is b True. aka is b False?
True

>>> c = None
>>> c is None
True
>>> c is not None
False
```

## `and`, `or`, and `not`

`and`, `or`, and `not` are the three basic types of boolean operators that are present in math, programming, and database logic.

In other programming languages, you might have seen the concept of `and` represented with `&&`, `or`, represented with `||`, and `not` represented by `!`. The Python language is instead focused on readability. So we'll use the english `and` instead of trying to remember fancy symbols. Python still uses the `&`, `|` and `!` expressions, but they're used for bitwise operations.

You can use them to compare one (or more expressions) and determine if they evaluate to `True` or `False`.

Thankfully, you don't have to be a computer scientist to understand them if you use this handy table.

### `and`, `or`, `not` Cheat Sheet

|Operation|Result|
|---|---|
|`a or b`|if a is `False`, then b, else a|
|`a and b`|if a is `False`, then a, else b|
|`not a`|if a is `False`, then `True`, else `False`|


### `and`

<!--
| a       	| b       	| a `and` b  	|
|---------	|---------	|------------	|
| `True`  	| `True`  	| **`True`** 	|
| `True`  	| False 	| False    	|
| False 	| `True`  	| False    	|
| False 	| False 	| False    	|
-->

{{% notice note %}}
For `a and b`, if a is false, a is returned. Otherwise b is returned.
*If `a and b` are both `bool`ean values, the expression evaluates to`True` if both a and b are `True`.*
{{% /notice %}}

```python
>>> a = True    # a is True
>>> b = True
>>> a and b     # True is returned. (value of b)
True

>>> False and True
False
>>> True and False
False
```

Notice what happens when we do the same thing to values that have a "truthiness" to them.

```python
>>> bool(0) # Verify that zero is "falsey"
False
>>> bool(1) # Verify that one is "truthy"
True
>>> 0 and 1 # 0 is False. 0 is returned.
0
```

### `or`

<!--
| a       	| b       	| a `or` b   	|
|---------	|---------	|------------	|
| `True`  	| `True`  	| **`True`** 	|
| `True`  	| False 	| **`True`** 	|
| False 	| `True`  	| **`True`** 	|
| False 	| False 	| False    	|
-->

{{% notice note %}}
For `a or b`, if a is false, b is returned. If a is true, a is returned.
*`a or b` evaluates to `True` if either (or both) of the expressions are true.*
{{% /notice %}}

```python
>>> True or True
True
>>> True or False
True
>>> False or False
False

>>> 0 or 1      # 0 is false. Return 1.
1
```

### `not`

| a       	| `not` a    	|
|---------	|------------	|
| `True`  	| `False`	|
| `False` 	| `True` 	|


{{% notice note %}}
`not a` reverses the `bool`ean value of `a`. If it *was* true, it will return `False`. If it was false, it will return `True`.
{{% /notice %}}

```python
>>> not True
False
>>> not False
True
```

### In Combination

When combining multiple boolean operators, you can add optional parentheses for readability. The operations in the inner-most parenthesis are evaluated first.

```python
>>> a = True
>>> b = True
>>> c = False

>>> a and (b or c)
True
```

You can combine multiple operators to test complex assumptions. For example, to return `True` only if *both* values are `False`, we can use the `not` negation operation on the result of an `or`.

```python
>>> a = False
>>> b = False

>>> a or b  # False because both are False.
False

>>> not (a or b)  # True - checking if both are False.
True
```

<!-- ### With "truthiness"

Remember, we learned that some values in Python are *falsey* like the number zero, and some are *truthy* like any number *expect* for zero.

It's a little counterintuitive, but when we compare values other than `bool`eans, our code behaves a little differently.

|Operation|Result|
|---|---|
|`x or y`|if x is false, then y, else x|
|`x and y`|if x is false, then x, else y|

Let's see it in action. First, lets test our assumptions again.

```python
>>> bool(0)     # Truthiness of 0 is False
False

>>> bool(1)     # Truthiness of 1 is True
True

>>> bool(None)  # Truthiness of None type is False
False

>>> 1 or 0      # Returns 1, the True value
1

>>> 1 and 0     # Returns 0, the False value
0

>>> 0 or None   # Neither are True. Returns nothing (None)
>>>
``` -->
