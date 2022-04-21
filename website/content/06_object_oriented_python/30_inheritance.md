+++
title = "Inheritance"
date = 2020-08-29T16:59:52-07:00
weight = 30
+++


Class inheritance is a very useful Object-oriented Programming construct for sharing and reusing code. Inheritance makes it possible to break up and organize your code into a hierarchy, from generic to specific. Objects that belong to classes that are higher up in the hierarchy (more generic) are accessible by subclasses, but not vice versa.

Earlier, we saw that `bool` is a subclass of `int`, thus, it *inherited* the properties and methods of the `int` class, and then *extended* it to be more specific to booleans.

We can do the same with our own classes, too. In a file called `vehicle.py`, let's create a parent `Vehicle` class, and have our `Car` class be a subclass.

```python
# vehicle.py

class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)

```

When we instantiate a Car instance, the interpreter calls `__init__()`, where we pass in two arguments (`make` and `model`) and an optional 3rd (`fuel`, which defaults to "gas"). In `__init__()`, we call `super().__init__()`, which resolves to our parent class, `Vehicle`, and runs *its* `__init__` function, where the variables are stored. Note that even though the variables are stored at the `Vehicle` level, they are instance variables because `self` is bound to `my_car`, which is a `Car`, which is a `Vehicle`. Don't forget to import your Vehicle and Car classes. Behold:

```python
# chapter_6.py

from vehicle import Vehicle, Car

my_car = Car("Ford", "Thunderbird")
print(f"my_car is type {type(my_car)}")
print(f"my_car uses {my_car.fuel}")

print(f"my_car is a Car: {isinstance(my_car, Car)}")
print(f"my_car is a Vehicle: {isinstance(my_car, Vehicle)}")
print(f"Car is a subclass of Vehicle: {issubclass(Car, Vehicle)}")
```

```bash
(env) $ python chapter_6.py
my_car is type <class 'vehicle.Car'>
my_car uses gas
my_car is a Car: True
my_car is a Vehicle: True
Car is a subclass of Vehicle: True
```

### Overriding Variables in a Subclass

We can, of course, use a subclass to override variables that belong to a parent class. Let's update our `vehicle.py` file:

```python
# vehicle.py

class Vehicle:
    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

class Car(Vehicle):

    def __init__(self, make, model, fuel="gas"):
        super().__init__(make, model, fuel)

class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

class Motorcycle(Vehicle):
    number_of_wheels = 2
```

```python
# chapter_6.py

from vehicle import Truck
 
my_truck = Truck("Ford", "F350")
print(f"my_truck is type {type(my_truck)}")
print(f"my_truck uses {my_truck.fuel}")
print(f"my_truck has {my_truck.number_of_wheels} wheels")
```

```bash
(env) $ python chapter_6.py
my_truck is type <class 'vehicle.Truck'>
my_truck uses diesel
my_truck has 6 wheels
```

Note how our Truck's class variable `number_of_wheels` overrode the parent class `Vehicle`'s `number_of_wheels` (or, to be more specific, the interpreter found `number_of_wheels` in a closer scope, the `Truck` class, and did not need to continue searching up the hierarchy). Likewise, `Motorcycle` overrides just the `number_of_wheels` variable to equal 2. Notice there is no `__init__()` function in `Motorcycle` - the `number_of_wheels` variable is overridden but instantiating a Motorcycle just goes straight to the `Vehicle.__init__()` method.


### Multiple Inheritance in Python

Can Python classes inherit from *multiple* parent classes? Yes, this is called *multiple inheritance*. It's not as commonly used for simple programs, but you'll see it more often as you start using libraries.

One common use case for multiple inheritance in Python is for a type of class called a *Mixin*. *Mixin* classes tend to be used to quickly and easily add additional properties and methods into a class. This type of design pattern encourages code with composable architecture.

Unfortunately, we won't have time to cover the topic of Multiple inheritance in this workshop... because it's *out of scope*. 🤣
