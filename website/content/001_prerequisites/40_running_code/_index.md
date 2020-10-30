+++
title = "Running Python Code"
date = 2020-08-29T17:46:35-07:00
weight = 40
+++

VS Code provides a built-in terminal that allows us to easily run our program or use Python's REPL.

## Running Code in Python Files

You know a file is a Python program when it ends with a `.py` extension.

#### Creating New Python Files

To create a new file in VS Code, hit `Ctrl + N` on Windows and Linux, or `Cmd + N` on macOS.

This will open a new file. Save the file with a `.py` extension.

#### Create Your First Program

{{% notice note %}}
Create a new simple Python program in a file called `hello.py` in your `pyworkshop` directory with the following contents:
{{% /notice %}}

```python
# in file: hello.py

greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")
```

### Running The File

You can run Python programs in one of 3 ways:
1. From VS Code
1. Directly from the terminal
1. As a shell script (covered in a later section)

#### 1. From VS Code

Once you've opened your `hello.py` file and selected your new terminal window, open the VS Code command palette.

{{% notice tip %}}
Open the command palette with `Ctrl + Shift + P` on Windows and Linux, and `Cmd + Shift + P` on Mac OS.
{{% /notice %}}

Then, select the following from the menu: **Python: Run Python File in Terminal**.

This should automatically open a new terminal window with the correct environment pre-selected and run your file.

#### 2. From the Terminal

##### Opening The VS Code Terminal Window

Next, you'll need to open your terminal if you don't have it open already. The quick keyboard shortcut to do that is <code>Ctrl + &#96;</code> (backtick).

Make sure your virtual environment is activated and you're in the correct directory then run the `python` command, adding in the filename.

```bash
(env) $ python hello.py
```


{{% notice tip %}}
To open a terminal in VS Code with the correct environment pre-selected, you can open the command palette and select **Python: Create Terminal**
{{% /notice %}}


##### Results

Run the code in your Python file both ways. 

You should see:

```bash
Hello, World!
Bonjour, World!
Hola, World!
```

How easy was that? 🎉


## Using the REPL

#### What's a REPL?

REPL stands for Read, Evaluate, Print, Loop. It allows you to interactively type in Python programs line-by-line.


There are many benefits to using a Python REPL. For one, it allows you to instantly see the output of your programs. You can also quickly catch mistakes as they're being made. Lastly, if you don't remember a bit of Python syntax, it's easy to quickly open a REPL and test your assumptions without needing to go through the hassle of running a full program. I make use of the REPL multiple times a day. 

In this class, we'll be using the REPL through the majority of the course to help us get familiar with Python syntax and data structures before moving on to running code in files.

You'll want to store code for reuse in files, while you can consider the REPL more of a scratch area. It's the place where you can instantly play around and try out Python code. The REPL is a handy tool for both beginner and advanced Python programmers.

### Open the REPL

#### From VS Code
Open the command palette in VS Code and select **Python: Start REPL**

#### From the terminal
If you'd like to start the REPL from the command line outside of the editor, type `python` in your shell, making sure that your environment is properly activated.

#### The Prompt

Note, in the REPL three arrows `>>>` indicate a line of input given at the prompt.

{{% notice warning %}}
If you see these `>>>` arrows in example code, don't copy them into your own REPL.
{{% /notice %}}

#### Getting Familiar


Let's get familiar with the REPL.

- `#` - comments start with `#`. They will be ignored.
- `>>>` - this is the prompt. In example code, lines starting with `>>>` means they are **input**
- lines that don't start with either of these are **output** that was produced by running input from the prompt

Start by typing these line of code at the `>>>` prompt, and press enter after each line.

```python
# My REPL. Don't copy the >>> symbols, that means the code was entered
# into the prompt.
#
# If the line does not start with >>>, that means it is output,
# not input
>>> name = "Nina"
>>> name
'Nina'
```

In the REPL, we can see the value of any variable just by entering it into the prompt.

You can copy and paste code into the REPL, even multiple lines of code at once. Copy the three lines below and paste them into your REPL. What's the result?

```python
x = 5
y = 33.5
x * y
```

{{%expand "See the result." %}}
```python
>>> x = 5
>>> y = 33.5
>>> x * y
167.5
```
{{% /expand%}}

The REPL allows us to gather information in real time about our Python program, which makes it a great learning tool.


{{% notice tip %}}
Press `Ctrl + D` to exit the repl.
{{% /notice %}}
