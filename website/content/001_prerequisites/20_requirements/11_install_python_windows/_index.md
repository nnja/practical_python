+++
title = "Windows Setup"
date = 2020-08-29T16:51:20-07:00
weight = 11
+++

For this course, you'll be using the latest stable version of Python available which is currently Python 3.9. 

{{% notice note %}}
You'll be using VS Code throughout the class to provide a consistent experience for all students. Once the course is over, feel free to go back to the editor of your choice to continue on your Python adventure.
{{% /notice %}}

{{% notice tip %}}
If you're used to keybindings in a different editor, you can set up a [keymaps extension](https://code.visualstudio.com/docs/getstarted/keybindings#_keymap-extensions) in VS Code to match what you're used to.
{{% /notice %}}

### Downloads

{{% button href="https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe" icon="fas fa-download" %}}Install Python3 from the Python.org{{% /button %}}

{{% button href="https://code.visualstudio.com/download" icon="fas fa-download" %}}Download Visual Studio Code{{% /button %}}
{{% button href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" icon="fas fa-download" %}}Python Extension for Visual Studio Code{{% /button %}}

### Making sure you're ready

To make sure you have all the prerequisites properly installed:

#### Install Python 3

Download and run the above installer. Be sure to select "Add Python 3.9 to PATH" on the first screen, and select Install Now. 

On the last page of the Python 3 installer, select “Disable Path Limit” before hitting close.

Close the installer.

From the Windows menu, search for PowerShell and right-click to Run as Administrator.

In the PowerShell window, type:

```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Enter Y for Yes.

#### Check for Python 3.9

In your open PowerShell window, type:

```powershell
> py -3.9
```

This should open a REPL window with a prompt.

{{% notice tip %}}
Type `exit()` followed by Enter to exit this screen and go back to your prompt, or use the keyboard shortcut `Ctrl+Z` and press Enter.
{{% /notice %}}


### Creating a Virtual Environment and The Project Folder

A Virtual Environments in Python is a self-contained directory that contains a Python installation for a particular version of Python.

It's a very useful way to make sure that we're using the right Python version when we're working on a particular project.

Let's create a project directory and a Python 3.9 Virtual Environment.

Using the same PowerShell terminal from earlier, type the following commands in one by one:

```powershell
> cd $home
> mkdir pyworkshop
> cd pyworkshop
> py -3.9 -m venv env
> .\env\Scripts\Activate
```

Your prompt should now look like this, but with your own username.

```powershell
(env) PS C:\Users\nina\pyworkshop>
```

#### Upgrade pip

Next, upgrade pip, the Python package installer to the latest version.

```powershell
python -m pip install --upgrade pip
```

{{% notice tip %}}
`env\Scripts\Activate` is how you *activate* your virtual environment in Windows. You'll want to do that each time you enter this Python project directory from a new shell.
{{% /notice %}}


### Troubleshooting

{{% notice warning %}}
You are expected to work from this project folder for the duration of the class, with an activated virtual environment.
{{% /notice %}}

If something is not working, please make sure that you're in the correct project directory with an activated virtual environment.

### Checking VS Code

Look for VS Code in your Applications, or type the following in your terminal.

```powershell
> code --version
```

You should see something like:

```text
1.49.0
e790b931385d72cf5669fcefc51cdf65990efa5d
x64
```

{{% notice info %}}
If you don't see VS Code, please follow the instructions for [installing VS Code](https://code.visualstudio.com/download) again.
{{% /notice %}}