# Programming the Robot

These tutorials take you from a brand new laptop all the way to running Python code on the real robot.

Our robot code is written in **Python** using **RobotPy**, which is the Python version of **WPILib** (the official FIRST Robotics Competition programming library). We write and run all of our code in **VS Code**.

## Before you start
You should have finished the **How to begin programming** tutorials first (at least Hello World through Defining A Function). You need to know what a variable, an `if` statement, a loop and a function are.

## Do these in order

| # | Tutorial | What you will be able to do at the end |
|---|----------|----------------------------------------|
| 1 | [Laptop Setup](01_LaptopSetup/laptopSetup.md) | Install Python, VS Code, Git and RobotPy |
| 2 | [Clone and Branch](02_CloneAndBranch/cloneAndBranch.md) | Get a copy of a team robot repository and make your own branch |
| 3 | [Your First Robot Project](03_FirstRobotProject/firstRobotProject.md) | Create a new robot project from scratch and understand each file |
| 4 | [The Robot Lifecycle](04_RobotLifecycle/robotLifecycle.md) | Explain when `Init`, `Periodic` and `Exit` methods run |
| 5 | [Running the Simulator](05_Simulator/simulator.md) | Run robot code on your laptop without a robot, and drive it with a controller or keyboard |
| 6 | [Testing Robot Code](06_TestingRobotCode/testingRobotCode.md) | Run automatic tests and write your own |
| 7 | [Debugging Robot Code](07_DebuggingRobotCode/debuggingRobotCode.md) | Pause robot code with breakpoints while the simulator is running |
| 8 | [Deploying to the Robot (roboRIO)](08_DeployToRobot/deployToRobot.md) | Put your code on the real robot and drive it |
| 8.2 | [Deploying to Systemcore (2027)](08.2_DeployToSystemcore/deployToSystemcore.md) | Update code for 2027, deploy to the new Systemcore controller, and drive with the FIRST Driver Station |

## Quick command cheat sheet
Run these in the VS Code terminal, **inside the folder that has `robot.py` in it**.

On Windows we type `py -m robotpy`. On Mac/Linux type `python3 -m robotpy` instead.

| Command | What it does | Needs internet? | Needs robot? |
|---------|--------------|-----------------|--------------|
| `py -m robotpy init` | Creates a new empty robot project | No | No |
| `py -m robotpy sync` | Installs the packages listed in `pyproject.toml` on your laptop and downloads the ones the robot needs | **Yes** | No |
| `py -m robotpy sim` | Runs your code in the simulator | No | No |
| `py -m robotpy test` | Runs automatic tests on your code | No | No |
| `py -m robotpy deploy` | Tests your code, then copies it to the robot and starts it | No | **Yes** |

> **2027 / Systemcore:** Tutorials 3-7 use RobotPy 2026 names like `teleopPeriodic`. RobotPy 2027 renamed them (for example to `teleop_periodic`). See [8.2, Part 2](08.2_DeployToSystemcore/deployToSystemcore.md) for the full list.

Stuck? Ask an experienced programming team member, a captain or a mentor. Everyone got stuck on this stuff the first time.
