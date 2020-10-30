+++
title = " Setup Checklist"
date = 2020-09-20T17:28:25-07:00
weight = 60
pre = "<b>✅  </b>"
+++

Make sure you're ready to start the course by checking off each requirement in the checklist.

{{% notice warning %}}
If you're missing a step, go back and follow the requirements for your operating system.
{{% /notice %}}

## Checklist

- [ ] Python > 3.9 installed
- [ ] VS Code installed
- [ ] Python Extension for VS Code installed
- [ ] Navigated to your project directory
- [ ] Created and activated Python Virtual Environment
- [ ] Opened VS Code in your project directory

## Get ready to start the course

Enter your `~/pyworkshop` directory from the terminal and start your already existing virtual environment.

### Get ready steps for Mac/Linux

```bash
$ python3 --version
Python 3.9.0

$ code --version
1.49.0
e790b931385d72cf5669fcefc51cdf65990efa5d
x64

$ cd ~/pyworkshop
$ source env/bin/activate

(env) $ code .
```

### Get ready steps for Windows (Powershell)

```powershell
> cd $home
> cd pyworkshop
> env\scripts\activate
```

### Open the REPL

Open the Command Palette in VS Code, and type: "Python: Start REPL"

{{% notice tip %}}
Remember, open the VS Code command palette with `Cmd + Shift + P` on Mac, `Ctrl + Shift + P` on Windows
{{% /notice %}}