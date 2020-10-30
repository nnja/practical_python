+++
title = "Configure VS Code"
date = 2020-08-29T16:49:45-07:00
weight = 30
+++

Visual Studio Code (commonly called VS Code) is a free, open source, lightweight cross platform code editor. A fresh installation is bare bones -- the power of VS Code comes via the extensions. There are useful extensions for every programming languages you can think of, but the choice of which ones to install and how to configure your editor is up to you.

By now you should have VS Code downloaded and installed. If not, please follow the setup instructions for your Operating System in this section.

## Python Extension

Next, we'll be downloading and installing the Python Extension. The Python Extension offers syntax highlighting, syntax checking, code auto-completion, and more.

 {{% button href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" icon="fas fa-download" %}}Python Extension for Visual Studio Code{{% /button %}}


## Keyboard Shortcuts

{{% notice note %}}
If you prefer keyboard shortcuts from a different editor, such as sublime, vim, or emacs, you can install a [key-map extension](https://code.visualstudio.com/docs/getstarted/keybindings#_keymap-extensions) to remap your keybindings.
{{% /notice %}}

To get started with VS Code, you only need to remember two keyboard shortcuts.

#### #1 : Show Command Palette

Open the command palette with `Ctrl + Shift + P` on Windows and Linux, and `Cmd + Shift + P` on macOS.

The command palette lets you search and run any of the commands available within VS Code. If you don't know how to do something, the command palette will usually point you in the right direction.

The command palette is how you'll navigate VS Code.

![Command Palette](/00_course_intro/images/command-palette.png?classes=shadow,border "The VS Code Command Palette")

#### #2 : Quick Open, Go to File

Open Quick Open with `Ctrl + P` on Windows and Linux, and `Cmd + P` on Mac OS.

Quick open is how you'll navigate your codebase and files.

**To dismiss either dialog, press the Escape key.**

{{% notice tip %}}
Write these two shortcuts down, because we'll be using them frequently for the rest of the course.
{{% /notice %}}

## Working With Files

{{% notice info %}}
Once we open our first Python file in VS Code, we'll see some configuration pop-ups. For the time being, **don't** dismiss them.
{{% /notice %}}

Create a new empty file, save it as `project.py`. 

Use Quick Open with `Ctrl + P` or `Cmd + P` to open the `project.py` file.

## Configuring The Interpreter

Many operating systems include Python, but unfortunately it's usually a few versions behind.

{{% notice warning %}}
We _never_ want to use Python2 for new Python projects, and we want to make sure we select the latest version of Python3 that we installed in the prerequisites.
{{% /notice %}}


Luckily, VS Code is smart. If you launch it from a directory with an *activated* virtual environment, it'll automatically pick up the correct interpreter. 

{{% notice tip %}}
Always check your interpreter version in the bottom bar before starting on your project. Yours should read `Python 3.9.0` or whichever version you installed earlier.
{{% /notice %}}



![Configure the Interpreter](/00_course_intro/images/vs-configure-interpreter.png?classes=shadow,border "The VS Code Python Extension Interpreter")

## Setting Up a Linter

Per the [VS Code documentation](https://code.visualstudio.com/docs/python/linting), linting highlights syntactical and stylistic problems in your Python source code. A linter will give you code hints about a variety of different types of problems. For example, when you have subtle errors in your code, like trying to use a variable you haven't defined yet. A linter will also show you when you're not following the Python style convention, called PEP8. PEP8 is a set of defined rules for how Python code should look. We'll cover it in more depth later, but what you need to know right now is that PEP8 warnings are not syntax errors. Even if your code doesn't adhere to the PEP8 standard, it may still run.

By default the linter will run every time you save a file, so it's good practice to save often with (`Ctrl + S` or `Cmd + S`).

Let's go ahead and click install on the Linter popup.

![Install pylint](/00_course_intro/images/vs-install-pylint.png?classes=shadow,border)

{{%expand "Note: If you accidentally dismissed the popup, expand this section for more details." %}}
Open the command palette and search for `Python: Select Linter`, then select `pylint`. The popup will now reappear, and you can hit install. 
![Select linter](/00_course_intro/images/vs-select-linter.png?classes=shadow,border)
![Choose pylint](/00_course_intro/images/vs-select-pylint.png?classes=shadow,border)
{{% /expand%}}

## (Optional) Install Pylance

Pylance is a new and improved language server for Python that makes intelligent code suggestions. These features are especially helpful to coders new to Python.

To use Pylance, [download the extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) and select "Yes" in the pop-up the first time you open a Python file. 

If you miss the pop-up, follow the instructions on the extension page to manually configure your preferred language server.