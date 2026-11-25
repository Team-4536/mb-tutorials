# 3. Your First Robot Project
In this tutorial you will create a robot project from nothing and learn what each file in it does.

## Goal
By the end you will have a working robot project that you made yourself, and you will know what `robot.py`, `pyproject.toml` and `.gitignore` are for.

## Prerequisites
* [2. Clone and Branch](../02_CloneAndBranch/cloneAndBranch.md). You should be on your own branch of **mb-tutorials**.
* Know what a **class** is. If you don't, that's OK. Read the "What is a class?" box below.

***
## Step 1. Make a folder for your project
1. In VS Code, in the **Explorer** (top icon on the left), make a new folder inside `Programming the Robot/03_FirstRobotProject/` named `yourName_robot`.
1. Open a terminal (**CTRL-SHIFT-`**) and move into that folder with `cd`:
```
cd "Programming the Robot/03_FirstRobotProject/yourName_robot"
```
> **Tip:** type `cd "Prog` and press **TAB**. The terminal fills in the rest of the name for you.

> **The #1 mistake:** robot commands only work when your terminal is **inside the folder that has `robot.py`**. If a command says it can't find `robot.py`, check where you are with `pwd` and use `cd` to get to the right folder.

***
## Step 2. Create the project
```
py -m robotpy init
```
You should see:
```
INFO : init : Created empty ...\robot.py
INFO : init : Created ...\pyproject.toml
INFO : init : Created ...\.gitignore
```

## Step 3. Install the right RobotPy version
```
py -m robotpy sync
```
`sync` reads `pyproject.toml` and does two things:
1. It installs the exact RobotPy version (and any extra packages) **on your laptop**.
2. It downloads the files the **robot** will need, so you can deploy later without internet.

> Run `sync` again any time `pyproject.toml` changes, and whenever you start working on a different robot project. It needs internet!

***
## What are these files?

### `pyproject.toml`: the shopping list
Open it. The important parts are:
```toml
[tool.robotpy]

# Version of robotpy this project depends on
robotpy_version = "2026.2.2"

# Which optional robotpy components should be installed?
components = [
    # "commands2",
    # "rev",
    ...
]

# Other pip packages to install, such as vendor packages
requires = []
```
* `robotpy_version` is the version of RobotPy the robot runs. **Everyone on the team should use the same one.** Your version number may be newer than this example, and that's fine.
* `components` are optional add-ons. You turn one on by deleting the `#` in front of it. For example, `"rev"` is for REV motor controllers (SPARK MAX) and `"phoenix6"` is for CTRE devices (Kraken/Falcon motors, CANcoders, Pigeon).
* `requires` is for any other Python packages the robot needs.

### `.gitignore`: files Git should NOT save
It lists files that are created automatically when you run code, like `__pycache__` folders and simulator settings. We don't commit those.

### `robot.py`: your robot!
Right now it just says `# TODO: insert robot code here`. Let's fix that.

***
## Step 4. Write your robot
> **What is a class?** A class is a blueprint for an object. `class MyRobot(wpilib.TimedRobot):` means "MyRobot is a kind of TimedRobot". WPILib already wrote all the hard parts of TimedRobot (talking to the Driver Station, timing, safety). We only fill in the methods we care about. `self` means "this robot", and we use it to remember things between method calls, like `self.timer`.

Replace everything in `robot.py` with:
```python
import wpilib


class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        print("Robot is starting up!")
        self.timer = wpilib.Timer()

    def teleopInit(self) -> None:
        print("Teleop started")
        self.timer.restart()

    def teleopPeriodic(self) -> None:
        wpilib.SmartDashboard.putNumber("Teleop Seconds", self.timer.get())
```
What it does:
* `import wpilib` loads the FRC library.
* `robotInit` runs **once** when the robot turns on. It makes a timer.
* `teleopInit` runs **once** each time the driver enables teleop. It restarts the timer at 0.
* `teleopPeriodic` runs **50 times a second** while teleop is enabled. It sends the timer's value to the dashboard.

(You'll learn exactly when every method runs in the next tutorial.)

## Step 5. Run it
```
py -m robotpy sim
```
A simulator window opens and the terminal shows `Robot is starting up!`. You'll learn to use this window in [Tutorial 5](../05_Simulator/simulator.md). For now, close the window (or click in the terminal and press **CTRL-C**) to stop the robot.

***
## Challenge
1. Change the message in `robotInit` to say your name.
1. Add a `teleopExit` method that prints `Teleop is over!` (it is spelled exactly like that: `def teleopExit(self) -> None:`).
1. Run the simulator, then commit and push `robot.py`, `pyproject.toml` and `.gitignore` on your branch.

**Next:** [4. The Robot Lifecycle](../04_RobotLifecycle/robotLifecycle.md)
