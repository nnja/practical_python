+++
title = "Virtual Environments"
date = 2020-08-29T17:03:53-07:00
weight = 30
+++

Virtual environments are a handy way to store the dependencies your Python application requires. Creating a virtual environment makes a self-contained folder that includes a full Python installation, allowing you to install dependencies specific to your application (or even a specific version of Python if you want) without relying on the global system version of Python.

As you saw earlier, you can create a virtual environment (or virtualenv for short) by running:

```bash
$ python3.9 -m venv env
$ source env/bin/activate
```

```powershell
> py -3.9 -m venv env
> .\env\Scripts\Activate
```

In either case, you've now created a folder called `venv` that includes a full Python install, and your shell is now set up to call this local Python version when you run the `python` command.

#### requirements.txt

`requirements.txt` is a special file that we use to tell `pip`, the Python package manager, which dependencies to install. The format is simple: you can create one manually by putting each dependency you import into a text file named `requirements.txt`, one dependency on each line.

Alternatively, you can install each dependency in your virtualenv using `pip`. Once you're done (your application stops complaining about missing imports), you can run:

```bash
$ pip freeze > requirements.txt
```

This will automatically generate a requirements.txt file for you, using the specific version of each dependency you installed in your virtualenv.

Later on, when you move your Python application to a new virtualenv, a new computer, or deploy it to the world, you can bring all your dependencies with you with requirements.txt. To install all your requirements again in a new virtual environment you can simply run:

```bash
$ pip install -r requirements.txt
```