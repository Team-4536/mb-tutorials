# 1. Laptop Setup for 2027 Robot Programming
In this tutorial you will check the tools needed to write, test and simulate MinuteBots robot code for the 2027 Systemcore.

## Goal
By the end you will have Python, VS Code, Git and RobotPy installed, and you will have proved that they all work.

## Prerequisites
* A computer running Windows, macOS or Linux. Update it first (Windows users: see [Updating Laptops](../../How%20to%20begin%20programming/Updating%20laptops/Updatinglaptops.md)).
* An internet connection (the MinuteBots wifi is fine, but **not** the robot's wifi, because the robot has no internet)
* Ask a mentor first if the laptop needs an administrator password to install programs

> **Team laptops:** many of these steps may already be done. Do the **"Check it"** step in each section first. If it works, skip to the next section.

***
## Step 1. Install Python 3.14

### Check it
Open a terminal. Use the command for your computer:

**Windows:**
```
py -3.14 --version
```

**macOS or Linux:**
```
python3 --version
```

For this tutorial, use Python **3.14.x**. If the command is missing or prints a different version, install the latest Python 3.14 release before continuing. On Windows and macOS, use the installer from [python.org](https://www.python.org/downloads/). On Linux, use your distribution's package manager and confirm `python3 --version` reports 3.14.

### Install it
1. On Windows, run the installer. **On the first screen, check "Add python.exe to PATH".**
1. Close and reopen the terminal, then repeat the version check above.

> **Why does the version matter?** RobotPy contains compiled libraries, so not every RobotPy release supports every Python release. RobotPy `2027.0.0a8` was tested here with Python 3.14.4; ask a mentor to confirm Python 3.14 is supported by the exact version the team has pinned. The Systemcore's Python is installed separately.

***
## Step 2. Install the Microsoft Visual C++ Redistributable (Windows only)
RobotPy uses some code written in C++, and Windows needs this package to run it. If it is missing, you will get confusing `DLL load failed` errors later.

1. Download **vc_redist.x64.exe** from [Microsoft](https://aka.ms/vs/17/release/vc_redist.x64.exe).
1. Run it. If it says it is already installed, that's fine. Click close.

On macOS and Linux, skip this step.

***
## Step 3. Install Git

### Check it
In the terminal type:
```
git --version
```
If you see something like `git version 2.x`, skip to Step 4.

### Install it
* **Windows:** download Git for Windows from [git-scm.com](https://git-scm.com/download/win), run the installer and accept the defaults.
* **macOS:** install Git from [git-scm.com](https://git-scm.com/download/mac) or install Apple's Command Line Tools.
* **Linux:** install Git using your distribution's package manager.

Open a **new** terminal and run `git --version` again.

***
## Step 4. Install VS Code and the Python extension

### Check it
Look for **Visual Studio Code** in the Start menu, Applications folder or app launcher. (VS Code is the blue icon. "Visual Studio" with a purple icon is a different program.)

### Install it
1. Download the installer for your operating system from [code.visualstudio.com](https://code.visualstudio.com/).
1. On Windows, run the installer. On the "Select Additional Tasks" screen, check **"Add to PATH"** and **"Add 'Open with Code' action"** for files and folders. On macOS, move VS Code to Applications, then use the Command Palette to run **Shell Command: Install 'code' command in PATH**. On Linux, use the package for your distribution.
1. Open a new terminal and run `code --version` to confirm the command works.

### Add the Python extension
1. Open VS Code.
1. Click the **Extensions** icon on the left side bar (it looks like four squares) or press **CTRL-SHIFT-X** (Windows/Linux) or **CMD-SHIFT-X** (macOS).
1. Search for `Python` and install the one made by **Microsoft**. It also installs **Pylance** and **Python Debugger**, which we use later.

***
## Step 5. Install RobotPy
RobotPy is the set of Python packages that lets Python control an FRC robot. Install the **exact 2027 version approved by the team**; an unpinned `pip install robotpy` may install the latest stable version instead of the team's 2027 version. Ask a mentor for the version in the current team project's `pyproject.toml`.

In VS Code, open a terminal with **Terminal --> New Terminal**. Upgrade pip and install the version your mentor gave you:

**Windows** (replace `2027.0.0a8` with the team's exact version):
```
py -3.14 -m pip install --upgrade pip
py -3.14 -m pip install "robotpy==2027.0.0a8"
```

**macOS** (replace `2027.0.0a8` with the team's exact version):
```
python3 -m pip install --upgrade pip
python3 -m pip install "robotpy==2027.0.0a8"
```
This downloads a lot of packages, so it can take a few minutes.

**Linux:** Prefer a virtual environment rather than installing into the operating-system Python. On Ubuntu, install Python 3.14 and its venv support (`sudo apt install python3.14 python3.14-venv`), then run:
```
python3 -m venv ~/robotpy-2027
source ~/robotpy-2027/bin/activate
python -m pip install --upgrade pip
python -m pip install "robotpy==2027.0.0a8"
```
Use `python -m robotpy ...` while the environment is active. Activate it again in each new terminal.

### Check it
**Windows:**
```
py -3.14 -m robotpy --help
```

**macOS:**
```
python3 -m robotpy --help
```
**Linux:** with the virtual environment active:
```
python -m robotpy --help
```
You should see a list of commands that includes `init`, `sim`, `sync`, `test` and `deploy`.

> **Linux note:** If `venv` is unavailable, install the matching Python 3.14 venv package from your distribution. Do not bypass the operating system's package protection.

> **Why `py -3.14 -m robotpy` instead of just `robotpy`?** It selects the Python version explicitly and runs the RobotPy module through that Python. On macOS, use `python3 -m robotpy` after confirming `python3 --version` reports Python 3.14. On Linux, activate the venv and use `python -m robotpy`.

***
## Step 6. Driver Station software
You do not need a Driver Station to run the simulator.

For the primary 2027 Systemcore path, install the **FIRST Driver Station** as described in [Tutorial 8](../08.2_DeployToSystemcore/deployToSystemcore.md). It supports Windows, macOS and Linux, but Linux may need extra input-device setup.

The older NI **FRC Driver Station** is for roboRIO projects and runs only on Windows. Use it only for the optional [legacy roboRIO tutorial](../08_DeployToRobot/deployToRobot.md), and ask a mentor which season's FRC Game Tools to install.

***
## Mac and Linux notes
* Skip the Microsoft Visual C++ Redistributable step.
* Use `python3` for RobotPy commands and confirm it is Python 3.14 before installing packages.
* On Linux, install the matching Python 3.14 `pip` and `venv` packages if they are not included with Python. Do not mix packages from different Python versions.
* The FIRST Driver Station supports macOS and Linux. Follow its current installation guide and ask a mentor for Linux input-device setup.

***
## Challenge
Show a mentor or captain a terminal that has the output of these commands (use the Windows or macOS/Linux command where noted):
```
git --version
code --version
```
On Windows, also run `py -3.14 --version` and `py -3.14 -m robotpy --help`. On macOS/Linux, run `python3 --version` and `python3 -m robotpy --help`.

**Next:** [2. Clone and Branch](../02_CloneAndBranch/cloneAndBranch.md)
