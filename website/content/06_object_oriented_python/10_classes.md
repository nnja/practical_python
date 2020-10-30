+++
title = "Classes"
date = 2020-08-29T16:59:44-07:00
weight = 10
+++

Every thing or object in Python is an instance of a *class*. The number `42` is an instance of the class `int`. The string `Hello, world` is an instance of the `str` (or string) class. These classes, in turn, are subclasses of the master `object` class.


### Classes vs Instances

The Object-oriented Programming paradigm is structured around Classes and Instances. You can think of a class as a "type" of something, like "Car." You can think of an instance as a specific thing, such as "my Subaru," which is a type of "Car." Both classes and instances can have variables and methods. Changing a class variable will change what is returned when you get that variable from an instance, however changing an instance variable only applies to that one instance. We'll come back to this in a second.


### `self`

You might have seen the `self` keyword peppered around in examples of Python objects. `self` is used inside classes to refer to a bound instance variable or object. For example, let's say we have a class called `Car`. Now, let's make a specific instance of our Car class and call the `start()` method on it to see if it starts. Start a new file named `chapter_6.py`

```python
# chapter_6.py

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"My car runs: {my_car.runs}")
my_car.start()
```

```bash
(env) $ python chapter_6.py
My car runs: True
Car is started. Vroom vroom!
```

We can see that the `runs` variable of our `my_car` instance is `True`. Now, what if we set `runs` to `False`?

```python
# chapter_6.py

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
my_car.runs = False
my_car.start()
```
```bash
(env) $ python chapter_6.py
Car is broken :(
```

But if we make a new instance of the `Car` class...

```python
# chapter_6.py

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
my_car.runs = False
my_car.start()

my_other_car = Car()
my_other_car.start()
```
```bash
(env) $ python chapter_6.py
My car runs: False
Car is broken :(
Car is started. Vroom vroom!
```

When we run the `start()` function, the `self` keyword points to the bound instance of `Car` - so when we call `start()` on `my_car`, self points to `my_car` and sees an instance variable `runs` that is `False`, but when we call `my_other_car.start()`, it returns `True`. Why?


### `self` refers to an instance

Back to what we were saying in the last section, `runs` is a class variable on the Car class, meaning that it exists for all instances of type Car. When we set `runs` to `False`, we created an instance variable on `my_car`, and when we called `start()`, `self` told the interpreter to look for an instance variable in `my_car` called `runs`.

When we called `my_other_car.start()`, the interpreter looked for an instance variable called `runs`, but didn't find it, so it looked at the next level up, the class, and found the class variable `Car.runs`, which returned `True`.

You may have noticed, but all instance methods within classes take `self` as their first argument, such as `def start(self):` above.

What happens if we call `start()` on the Car class instead of an instance?

```python
# chapter_6.py

class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

Car.start()
```

```bash
(env) $ python chapter_6.py
Traceback (most recent call last):
  File "chapter_6.py", line 10, in <module>
    Car.start()
TypeError: start() missing 1 required positional argument: 'self'
```

If you try to call `start()` on the Car class, `self` doesn't have an instance to bind to, so we get an error that the required argument `self` wasn't passed in to the `start()` function.