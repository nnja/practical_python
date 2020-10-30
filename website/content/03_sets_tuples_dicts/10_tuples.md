+++
title = "Tuples"
date = 2020-08-29T16:54:36-07:00
weight = 10
+++

Tuples are light-weight collections used to keep track of related, but different items. Tuples are **immutable**, meaning that once a tuple has been created, the items in it can't change. You can't add, remove, or update items like you can with a list.

### `tuple` cheat sheet

| type               	| `tuple`                                                                                                 	|
|--------------------	|---------------------------------------------------------------------------------------------------------	|
| use                	| Used for storing a snapshot of related items when we don't plan on modifying, adding, or removing data. 	|
| creation           	| `()` or `tuple()` for empty tuple. `(1, )` for one item, or `(1, 2, 3)` for a tuple with several items.  	|
| search methods     	| `my_tuple.index(item)` or `item in my_tuple`                                                            	|
| search speed       	| Searching for an item in a large tuple is slow. Each item must be checked.                              	|
| common methods     	| Can't add or remove from tuples.                                                                        	|
| order preserved?   	| Yes. Items can be accessed by index.                                                                    	|
| mutable?           	| **No**                                                                                                  	|
| in-place sortable? 	| **No**                                                                                                  	|

### Uses

You might ask, why `tuple` when Python already has lists? `tuple` is different in a few ways. While lists are generally used to store collections of similar items together, `tuple`s, by contrast, can be used to contain a snapshot of data. A good use of a `tuple` might be for storing the information for a *row* in a spreadsheet. We don't necessarily care about updating or manipulating that data, we just want a read-only snapshot.

`tuple` is an interesting and powerful datatype, and one of the more unique aspects of Python. Most other programming languages have ways of representing lists and dictionaries, but only a small subset contain tuples. Use them to your advantage.

### Examples

#### Empty and one-item `tuple`s

One important thing to note about tuples is that there's a quirk to their creation. Let's check the type of an empty `tuple` created with `()`.
```python
>>> a = ()
>>> type(a)
<class 'tuple'>
```

That looks like we'd expect it to. What about if we *tried* to create a one-item `tuple` using the same syntax?

```python
>>> b = (1)
>>> type(b)
<class 'int'>
```

It didn't work! `type((1))` is an `int`. In order to create a one-item tuple, you'll need to include a trailing comma inside the parenthesis.

```python
>>> c = (1, )
>>> type(c)
<class 'tuple'>
```

{{% notice tip %}}
If you're creating a one-item tuple, you **must** include a trailing comma, like this: `(1, )`
{{% /notice %}}

#### Creation

Let's say we have a spreadsheet of students, and we'd like to represent each row as a tuple.

```python
>>> student = ("Marcy", 8, "History", 3.5)
```

#### Access by index

We can access items in the `tuple` by index.

```python
>>> student = ("Marcy", 8, "History", 3.5)
>>> student[0]
'Marcy'
```

But if we try to change the contents, we'll get an error. Remember, you can't change the items in a tuple.

```python
>>> student[0] = "Bob"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

{{% notice info %}}
We'll see `TypeError: 'tuple' object does not support item assignment` if we try to change the items in a tuple.
{{% /notice %}}

Tuples also don't have an `append` or `extend` method available on them like lists do, because they can't be changed.

### `tuple` unpacking.

Sounds like a lot of work for not a lot of benefit, right? Not so. `tuple` is great when you depend on your data staying unchanged. Because of this guarantee, we can use `tuple`s in other types of containers like `set`s and `dict`ionaries that expect immutable keys. We'll learn more about this later in the chapter.

It's also a great way to quickly consolidate information.

You can also use `tuple`s for something called unpacking. Let's see it in action:

```python
>>> student = ("Marcy", 8, "History", 3.5)
>>>
>>> name, age, subject, grade = student
>>> name
'Marcy'
>>> age
8
>>> subject
'History'
>>> grade
3.5
```

You can return tuples from functions, and use unpacking to get the values back.

```python
>>> def http_status_code():
...     return 200, "OK"
...
>>> code, value = http_status_code()
>>> code
200
>>> value
'OK'
```