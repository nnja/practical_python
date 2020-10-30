+++
title = "Philosophy"
date = 2020-08-29T16:52:25-07:00
weight = 20
+++

The Zen of Python is a collection of 19 software principles written in a poem that influences the design of Python Programming Language. It was published on the Python mailing list in June 1999 by Tim Peters. [*](https://en.wikipedia.org/wiki/Zen_of_Python)

### Zen of Python in The Python Interpreter

The Zen of Python is included as an easter egg in the Python REPL. You can read it by typing `import this` in our REPL, to learn a little more about the principles and philosophy behind Python.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
...
```

#### Simple is Better Than Complex

Generally, Python programmers prefer to be explicit and write *simple*, *understandable*, and *maintainable* code instead of ego flexing and writing unnecessarily complex code.

#### Readability Counts

Make your code easy to read. Avoid single character variable names. Call your functions with named parameters where applicable. Use good variable names.

### Focus on simple, readable code

Python encourages you to write simple, readable code by following a style-guide called PEP8.

[PEP8](https://pep8.org/) is a Python coding standard, that sets guidelines for how our Python code should look and be formatted.

Tools called linters will identify when your code doesn't meet PEP8 standards. The warnings that linters give aren't syntax errors. Your code will still run, but it won't meet Python code style standards.


#### More Easter Eggs

{{% notice note %}}
To see another Python easter egg, type the following into your REPL: `from __future__ import braces`
{{% /notice %}}

{{%expand "You'll see the following: 🤣" %}}
```python
>>> from __future__ import braces
  File "<stdin>", line 1
SyntaxError: not a chance
```
{{% /expand%}}

{{% notice note %}}
My favorite Easter Egg? Type `import antigravity` into the REPL.
{{% /notice %}}

![](/images/python.png)
