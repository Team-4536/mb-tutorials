# Programming the Robot

These tutorials take you from a brand new laptop through writing, testing and simulating Python robot code, then prepare you to deploy to the 2027 Systemcore.

Our robot code is written in **Python** using **RobotPy**, the Python version of **WPILib** (the official FIRST Robotics Competition programming library). We write and run all of our code in **VS Code**. These tutorials use the **2027 RobotPy API**; get the exact RobotPy version from a mentor or the current team project before installing it.

## Before you start
You should have finished the **How to begin programming** tutorials first (at least Hello World through Defining A Function). You need to know what a variable, an `if` statement, a loop and a function are.

## Do these in order

| # | Tutorial | What you will be able to do at the end |
|---|----------|----------------------------------------|
| 1 | [Laptop Setup](01_LaptopSetup/laptopSetup.md) | Install Python 3.14, VS Code, Git and the team-pinned RobotPy |
| 2 | [Clone and Branch](02_CloneAndBranch/cloneAndBranch.md) | Get a copy of a team robot repository and make your own branch |
| 3 | [Your First Robot Project](03_FirstRobotProject/firstRobotProject.md) | Create a 2027 robot project from scratch and understand each file |
| 4 | [The Robot Lifecycle](04_RobotLifecycle/robotLifecycle.md) | Explain when the 2027 `init`, `periodic` and `exit` methods run |
| 5 | [Running the Simulator](05_Simulator/simulator.md) | Run robot code on your laptop without a robot, drive it with a controller or keyboard, and view NetworkTables |
| 6 | [Testing Robot Code](06_TestingRobotCode/testingRobotCode.md) | Run automatic tests and write your own |
| 7 | [Debugging Robot Code](07_DebuggingRobotCode/debuggingRobotCode.md) | Pause robot code with breakpoints while the simulator is running |
| 8 | [Deploying to Systemcore (2027)](08.2_DeployToSystemcore/deployToSystemcore.md) | Deploy your 2027 code and drive with the FIRST Driver Station |
| Optional | [Deploying to a roboRIO (2026 and earlier)](08_DeployToRobot/deployToRobot.md) | Follow this legacy path only when working with a roboRIO and a matching 2026-or-earlier project |

## Quick command cheat sheet
Run these in the VS Code terminal, **inside the folder that has `robot.py` in it**. Use the same Python 3.14 installation you checked in Tutorial 1.

This cheat sheet uses `python3`; on Windows, replace it with `py -3.14`. The detailed tutorials use the Windows form `py -3.14`; on macOS/Linux, replace that prefix with `python3`. In all cases, confirm the command selects Python 3.14.

| Command | What it does | Needs internet? | Needs robot? |
|---------|--------------|-----------------|--------------|
| `python3 -m robotpy init` | Creates a new empty robot project | No | No |
| `python3 -m robotpy sync` | Installs the exact packages listed in `pyproject.toml` and downloads the ones the Systemcore needs | **Yes** | No |
| `python3 -m robotpy sim` | Runs your code in the simulator | No | No |
| `python3 -m robotpy test` | Runs automatic tests on your code | No | No |
| `python3 -m robotpy deploy` | Tests your code, then copies it to the Systemcore and starts it | No | **Yes** |

> RobotPy 2027 uses `snake_case` names such as `teleop_periodic`. The tutorials use those names from the start. The current `RobotCode/robotPeriodicAndInit` project is a historical RobotPy 2025 example; do not use it as the version reference for these lessons.

> RobotPy 2027 was prerelease software when this guide was prepared. Do not copy a prerelease number from an example: use the exact version pinned by the team project or confirmed by a mentor.

Stuck? Ask an experienced programming team member, a captain or a mentor. Everyone got stuck on this stuff the first time.
