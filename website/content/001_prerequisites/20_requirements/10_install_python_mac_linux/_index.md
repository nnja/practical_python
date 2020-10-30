+++
title = "Mac / Linux Setup"
date = 2020-08-29T16:51:20-07:00
weight = 10
+++

For this course, you'll be using the latest stable version of Python available, which is currently Python 3.9.


{{% notice note %}}
We'll be using VS Code throughout the class to provide a consistent experience for all students. Once the course is over, feel free to go back to the editor of your choice to continue on your Python adventure.
{{% /notice %}}


{{% notice tip %}}
If you're used to keybindings in a different editor, you can set up a [keymaps extension](https://code.visualstudio.com/docs/getstarted/keybindings#_keymap-extensions) in VS Code to match what you're used to.
{{% /notice %}}

### Downloads

{{% button href="https://www.python.org/downloads/" icon="fas fa-download" %}}Download Python3{{% /button %}}
{{% button href="https://code.visualstudio.com/download" icon="fas fa-download" %}}Download Visual Studio Code{{% /button %}}
{{% button href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" icon="fas fa-download" %}}Python Extension for Visual Studio Code{{% /button %}}

### Making sure you're ready

To make sure you have all the prerequisites properly installed:

#### Check for Python 3.9

Type the following on your terminal.
```bash
$ python3 --version
```

You should see something like
```bash
Python 3.9.0
```

{{% notice info %}}
If you don't see a Python version greater than 3.9, please follow the instructions for [installing Python3](https://www.python.org/downloads/) again.
{{% /notice %}}


### Creating a Virtual Environment and The Project Folder

A Virtual Environments in Python is a self-contained directory that contains a Python installation for a particular version of Python.

It's a very useful way to make sure that we're using the right Python version when we're working on a particular project.

Let's create a project directory and a Python 3.9 Virtual Environment.

Open a terminal window. Type the following.

(Do not type the `$` character, that signifies a prompt.)

```bash
$ cd ~
$ mkdir pyworkshop
$ cd pyworkshop
$ python3 -m venv env
$ source env/bin/activate
```

{{% notice tip %}}
`source env/bin/activate` is how you *activate* your virtual environment on Mac or Linux. You'll want to do that each time you enter this Python project directory from a new shell.
{{% /notice %}}

Your prompt should look like this to indicate that the virtual environment is active.

```bash
(env) $
```

#### Upgrade pip

Upgrade pip, the Python package installer to the latest version.

```bash
(env) $ python3 -m pip install --upgrade pip
```

### Troubleshooting

{{% notice warning %}}
You are expected to work from this project folder for the duration of the class, with an activated virtual environment.
{{% /notice %}}

If something is not working, please make sure that you're in the correct project directory with an activated virtual environment.

### Checking VS Code

Look for VS Code in your Applications, or type the following in your terminal.

```bash
$ code --version
```

You should see something like:

```text
1.49.0
e790b931385d72cf5669fcefc51cdf65990efa5d
x64
```

### Installing `code` on your Path

If typing `code` in your terminal doesn't work, you may need to follow the instructions to install it on your path, [here](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).

{{% notice info %}}
If you don't see VS Code, please follow the instructions for [installing VS Code](https://code.visualstudio.com/download) again.
{{% /notice %}}