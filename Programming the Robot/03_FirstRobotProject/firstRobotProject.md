# 3. Your First 2027 Robot Project
In this tutorial you will create a RobotPy 2027 project from nothing and learn what each file in it does.

## Goal
By the end you will have a working robot project that you made yourself, and you will know what `robot.py`, `pyproject.toml` and `.gitignore` are for.

## Prerequisites
* [2. Clone and Branch](../02_CloneAndBranch/cloneAndBranch.md). You should be on your own branch of **mb-tutorials**.
* RobotPy 2027 installed as described in [Tutorial 1](../01_LaptopSetup/laptopSetup.md), using the exact version approved by a mentor.
* Know what a **class** is. If you don't, that's OK. Read the "What is a class?" box below.

***
## Step 1. Make a folder for your project
1. In VS Code, in the **Explorer** (top icon on the left), make a new folder inside `Programming the Robot/03_FirstRobotProject/` named `yourName_robot`.
1. Open a terminal (**Terminal --> New Terminal**) and move into that folder with `cd`:
```
cd "Programming the Robot/03_FirstRobotProject/yourName_robot"
```
> **Tip:** type `cd "Prog` and press **TAB**. The terminal fills in the rest of the name for you.

> **The #1 mistake:** robot commands only work when your terminal is **inside the folder that has `robot.py`**. If a command says it can't find `robot.py`, check where you are with `pwd` and use `cd` to get to the right folder.

***
## Step 2. Create the project
```
py -3.14 -m robotpy init
```
You should see:
```
INFO : init : Created empty ...\robot.py
INFO : init : Created ...\pyproject.toml
INFO : init : Created ...\.gitignore
```

## Step 3. Check and install the right RobotPy version
Open `pyproject.toml` and check `robotpy_version`. It must match the exact version the team is using. `robotpy init` writes the version of the RobotPy command you installed, so correct it if it does not match the mentor's version.

The version below is an example of a 2027 prerelease that was tested while writing these tutorials. **Do not assume it is the team's approved version.**
```toml
robotpy_version = "2027.0.0a8"
```

Then run:
```
py -3.14 -m robotpy sync
```
`sync` reads `pyproject.toml` and does two things:
1. It installs the exact RobotPy version (and any extra packages) **on your laptop**.
2. It downloads the files the **Systemcore** will need, so you can deploy later without internet.

> Run `sync` again any time `pyproject.toml` changes, and whenever you start working on a different robot project. It needs internet!
>
> On Windows, use `py -3.14 -m robotpy ...`. On macOS/Linux, use `python3 -m robotpy ...` after checking that `python3` is Python 3.14.

***
## What are these files?

### `pyproject.toml`: the shopping list
Open it. The important parts are:
```toml
[tool.robotpy]

# Version of RobotPy this project depends on; replace with the team's exact pin
robotpy_version = "2027.0.0a8"

# Which optional robotpy components should be installed?
components = [
    # "commands2",
    # "sim",
]

# Other pip packages to install, such as vendor packages
requires = []
```
* `robotpy_version` is the version of RobotPy the robot runs. **Everyone on the team should use the same one.** Replace the example with the version pinned by a mentor or the current team project.
* `components` are optional add-ons. For 2027, ask a mentor which vendor packages belong in `requires`; the 2027 package layout differs from older RobotPy projects.
* `requires` is for any other Python packages the robot needs.

### `.gitignore`: files Git should NOT save
It lists files that are created automatically when you run code, like `__pycache__` folders and simulator settings. We don't commit those.

### `robot.py`: your robot!
Right now it just says `# TODO: insert robot code here`. Let's fix that.

***
## Step 4. Write your robot
> **What is a class?** A class is a blueprint for an object. `class MyRobot(wpilib.TimedRobot):` means "MyRobot is a kind of TimedRobot". WPILib already wrote the timing and Driver Station integration. We fill in the methods we care about. In 2027, `__init__` sets up the robot object; `self` lets us remember things between method calls, like `self.timer`.

Replace everything in `robot.py` with:
```python
import ntcore
import wpilib


class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.timer = wpilib.Timer()
        table = ntcore.NetworkTableInstance.get_default().get_table("Tutorial")
        self.teleop_seconds = table.get_double_topic("Teleop Seconds").publish()

    def teleop_init(self) -> None:
        print("Teleop started")
        self.timer.restart()

    def teleop_periodic(self) -> None:
        self.teleop_seconds.set(self.timer.get())
```
What it does:
* `import wpilib` loads the FRC library.
* `__init__` runs when WPILib creates the robot object. `super().__init__()` must be first.
* `teleop_init` runs once each time teleop starts. It restarts the timer at 0.
* `teleop_periodic` runs about 50 times a second while teleop is enabled. It publishes the timer value under the `Tutorial` NetworkTables table.
* The underscore names are the RobotPy 2027 API. In older code you may see camelCase names such as `teleopPeriodic`.

(You'll learn exactly when every method runs in the next tutorial.)

## Step 5. Run it
```
py -3.14 -m robotpy sim
```
A simulator window opens. You will learn to use it in [Tutorial 5](../05_Simulator/simulator.md). For now, close the window (or click in the terminal and press **CTRL-C**) to stop the robot.

***
## Challenge
1. Change the message in `teleop_init` to include your name.
1. Add a `teleop_exit` method that prints `Teleop is over!` (use the 2027 spelling: `def teleop_exit(self) -> None:`).
1. Run the simulator, then commit and push `robot.py`, `pyproject.toml` and `.gitignore` on your branch.

**Next:** [4. The Robot Lifecycle](../04_RobotLifecycle/robotLifecycle.md)
