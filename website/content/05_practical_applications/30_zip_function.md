+++
title = "Zip"
date = 2020-08-29T16:58:58-07:00
weight = 30
+++

It's often necessary to iterate over multiple lists simultaneously. Suppose we're keeping score of a game and we have two lists, one for names and one for scores:

```python
>>> names = ["Bob", "Alice", "Eve"]
>>> scores = [42, 97, 68]
```

The `zip` function takes any number of iterable arguments and steps through
all of them at the same time until the end of the *shortest* iterable has been reached:

```python
>>> for name, score in zip(names, scores):
>>>     print(f"{name} had a score of {score}.")
...
Bob had a score of 42.
Alice had a score of 97.
Eve had a score of 68.
```

What will the above loop print after removing the last element from `scores`?

```python
>>> scores.pop(-1)
68
>>> for name, score in zip(names, scores):
>>>     print(f"{name} had a score of {score}.")
...
Bob had a score of 42.
Alice had a score of 97.
```

The loop terminates even though there are more values in `names`. Here, Eve isn't included because `scores` only has two elements.

We can also use `zip()` to quickly and easily create a `dict` from two lists.

```python
>>> names = ["Bob", "Alice", "Eve"]
>>> scores = [42, 97, 68]

>>> score_dict = dict(zip(names, scores))

>>> print(score_dict)
{'Bob': 42, 'Alice': 97, 'Eve': 68}
```

Note that the result of calling the zip function is actually a generator under the hood. You can only loop over the result of zipping once. If you try to loop over it again, the result will be empty.

```python
>>> names = ["Bob", "Alice", "Eve"]
>>> scores = [42, 97, 68]
>>> zip_result = zip(names, scores)

# Works fine the first time!
>>> for name, score in zip_result:
...     print(f"{name} had a score of {score}.")
...
Bob had a score of 42.
Alice had a score of 97.
Eve had a score of 68.

# But empty if we try to loop over it again.
>>> for name, score in zip_result:
...     print(f"{name} had a score of {score}.")
...
>>>
```