# 1. Laptop Setup for Robot Programming
In this tutorial you will install everything a laptop needs to write and run MinuteBots robot code.

## Goal
By the end you will have Python, VS Code, Git and RobotPy installed, and you will have proved that they all work.

## Prerequisites
* A Windows laptop that is up to date (see [Updating Laptops](../../How%20to%20begin%20programming/Updating%20laptops/Updatinglaptops.md))
* An internet connection (the MinuteBots wifi is fine, but **not** the robot's wifi, because the robot has no internet)
* Ask a mentor first if the laptop needs an administrator password to install programs

> **Team laptops:** many of these steps may already be done. Do the **"Check it"** step in each section first. If it works, skip to the next section.

***
## Step 1. Install Python

### Check it
1. Open a terminal. In Windows, press the Windows key, type `terminal` (or `powershell`) and press enter.
1. Type this and press enter:
```
py --version
```
If you see `Python 3.13.x` or `Python 3.14.x`, Python is installed. Skip to Step 2.

If you see `'py' is not recognized` or a version lower than 3.10, keep going.

### Install it
1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest Python 3 for Windows.
1. Run the installer. **On the very first screen, check the box that says "Add python.exe to PATH".**
1. Click **Install Now** and wait for it to finish.
1. Close the terminal, open a new one and run `py --version` again.

> **Why does the version matter?** RobotPy only works with certain Python versions. Right now that is Python 3.10 through 3.14. The Python on the robot is installed separately, so your laptop's version doesn't need to match it exactly.

***
## Step 2. Install the Microsoft Visual C++ Redistributable
RobotPy uses some code written in C++, and Windows needs this package to run it. If it is missing, you will get confusing `DLL load failed` errors later.

1. Download **vc_redist.x64.exe** from [https://aka.ms/vs/17/release/vc_redist.x64.exe](https://aka.ms/vs/17/release/vc_redist.x64.exe)
1. Run it. If it says it is already installed, that's fine. Click close.

***
## Step 3. Install Git

### Check it
In the terminal type:
```
git --version
```
If you see something like `git version 2.x`, skip to Step 4.

### Install it
1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) and download Git for Windows.
1. Run the installer. Clicking **Next** on every screen (the default choices) is fine.
1. Open a **new** terminal and run `git --version` again.

***
## Step 4. Install VS Code and the Python extension

### Check it
Look for **Visual Studio Code** in the Start menu. (VS Code is the blue icon. "Visual Studio" with a purple icon is a different program.)

### Install it
1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/) and download VS Code for Windows.
1. Run the installer. On the "Select Additional Tasks" screen, check **"Add 'Open with Code' action"** for files and folders. It is very handy.

### Add the Python extension
1. Open VS Code.
1. Click the **Extensions** icon on the left side bar (it looks like four squares) or press **CTRL-SHIFT-X**.
1. Search for `Python` and install the one made by **Microsoft**. It also installs **Pylance** and **Python Debugger**, which we use later.

***
## Step 5. Install RobotPy
RobotPy is the set of Python packages that lets Python control an FRC robot.

1. In VS Code, open a terminal: **Terminal --> New Terminal** (or **CTRL-SHIFT-`**).
1. Type:
```
py -m pip install --upgrade pip
py -m pip install robotpy
```
This downloads a lot of packages, so it can take a few minutes.

### Check it
```
py -m robotpy --help
```
You should see a list of commands that includes `init`, `sim`, `sync`, `test` and `deploy`.

> **Why `py -m robotpy` instead of just `robotpy`?** `py -m` means "use the Python I installed to run this module". It works even when Windows can't find the `robotpy` command on its own, so we always use it.

> **Which version of RobotPy?** Don't worry about it yet. Every robot project has a `pyproject.toml` file that says exactly which version it needs, and in Tutorial 3 you will run `py -m robotpy sync` to install that exact version.

***
## Step 6 (only needed to drive the real robot). Install the FRC Driver Station
You don't need this for the simulator. You need it for [Tutorial 8](../08_DeployToRobot/deployToRobot.md), when you drive the real robot.

The FRC Driver Station only runs on **Windows**. It comes in the **FRC Game Tools** download from National Instruments. Ask a mentor which version to install, because it has to match the software on the robot for this season.

***
## Mac and Linux users
Everything works the same with two changes:
* Install Python from python.org (Mac) or your package manager (Linux). Skip Step 2.
* Type `python3` wherever these tutorials say `py`. For example: `python3 -m pip install robotpy` and `python3 -m robotpy --help`.

The Driver Station does not run on Mac or Linux. Use a Windows laptop to drive the real robot.

***
## Challenge
Show a mentor or captain a terminal that has the output of all four of these commands:
```
py --version
git --version
code --version
py -m robotpy --help
```

**Next:** [2. Clone and Branch](../02_CloneAndBranch/cloneAndBranch.md)
