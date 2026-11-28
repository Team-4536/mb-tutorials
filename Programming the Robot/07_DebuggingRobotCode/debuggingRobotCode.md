# 7. Debugging 2026 Robot Code
The [debugger tutorial](../../debugger%20tutorial.md) showed you breakpoints and stepping through a normal Python file. Robot code is a little different: you don't run `robot.py` directly, you run `robotpy sim`. In this tutorial you will set up VS Code so the debugger can pause robot code while the simulator is running.

## Goal
By the end you will be able to press **F5** to start the simulator in the debugger, stop on a breakpoint inside `teleop_periodic`, look at variables, and debug a test.

## Prerequisites
* [debugger tutorial](../../debugger%20tutorial.md) (how breakpoints, step over, step into and continue work)
* [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md)
* The **Python** extension from Microsoft installed in VS Code (from [Tutorial 1](../01_LaptopSetup/laptopSetup.md))
* VS Code selected the Python 3.14 interpreter where the team's RobotPy version is installed

***
## Step 1. Make a `launch.json`
`launch.json` tells VS Code **how** to start your program when you press F5.

1. Click the **Run and Debug** icon on the left side bar (a play button with a bug).
1. Click **create a launch.json file**. If VS Code asks you to pick a debugger, choose **Python Debugger**, then **Python File**.
1. VS Code creates and opens `.vscode/launch.json`. Replace **everything** in it with:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "RobotPy: Simulate",
            "type": "debugpy",
            "request": "launch",
            "module": "robotpy",
            "args": ["sim"],
            "cwd": "${fileDirname}",
            "justMyCode": true
        },
        {
            "name": "RobotPy: Test",
            "type": "debugpy",
            "request": "launch",
            "module": "robotpy",
            "args": ["test", "--no-isolation"],
            "cwd": "${fileDirname}",
            "justMyCode": true
        }
    ]
}
```
What these settings mean:
* `"module": "robotpy"` and `"args": ["sim"]` mean "run the RobotPy simulator using the Python interpreter selected in VS Code".
* `"cwd": "${fileDirname}"` means "run it in the folder of the file I have open right now". **So open `robot.py` (click on its tab) before you press F5.**
* `"--no-isolation"` makes the tests run inside the debugger. Normally each test runs in its own separate process, and the debugger can't see into those.
* `"justMyCode": true` means "only stop in our code, not inside WPILib".

> If the robot repo already has a `.vscode/launch.json`, just add these two configurations to its `"configurations"` list.

***
## Step 2. Set a breakpoint and start debugging
Use the controller robot from [Tutorial 5](../05_Simulator/simulator.md).

1. Open `robot.py`. Click to the left of the line number on `self.motor.set_throttle(speed)` so a **red dot** appears.
1. At the top of **Run and Debug**, choose **RobotPy: Simulate** from the dropdown, then press the green play button (or press **F5**).
1. The simulator opens like normal. Connect Keyboard 0 to Joystick[0] and click **Teleoperated**.
1. VS Code jumps to the front and highlights the breakpoint line. The robot is paused!

## Step 3. Look around
* In the **Variables** panel on the left, open **Locals**. What is `speed`?
* Open `self` to see everything your robot remembers: `controller`, `motor`...
* Hover your mouse over `speed` in the code to see its value.
* Press **F5** (Continue). It stops again on the very next loop, 20 ms later. Hold W in the simulator and press F5 again. Did `speed` change?
* Click the red dot again to remove the breakpoint, then press F5. The robot keeps running.
* Press the red square (**Stop**, or **SHIFT-F5**) to stop the robot.

> **Pausing the robot freezes time.** While you are stopped on a breakpoint, no loops run. The simulator window may stop responding, and you'll see `Loop time overrun` warnings when you continue. That's normal in the simulator. **Never** do this on the real robot while it's moving.

### Conditional breakpoints
Stopping on every loop gets annoying. Right-click the red dot, choose **Edit Breakpoint...**, choose **Expression**, and type:
```
speed > 0.5
```
Now it only stops when the stick is pushed more than halfway.

***
## Step 4. Debug a test
1. Open your test file (for example `tests/teleop_test.py`) and set a breakpoint on the `assert` line.
1. Choose **RobotPy: Test** in the dropdown. **Click on the `robot.py` tab** so the robot's folder is the current folder, then press F5.
1. When it stops, look at `robot` in the Variables panel. You can see exactly what the robot was doing when the test checked it.

***
## Historical team example
The [`RobotCode/robotPeriodicAndInit/src`](../../RobotCode/robotPeriodicAndInit/src) project is pinned to RobotPy 2026 and is not part of this 2026 run path. You can read its `subsystemManager.py` to see how a manager iterates over subsystems, but do not launch or debug it with the 2026 environment.

***
## Challenge
In the archived [`subsystemManager.py`](../../RobotCode/robotPeriodicAndInit/src/subsystemManager.py), find which subsystem appears twice in the list. Use the debugger on your 2026 project to inspect a value changing once per periodic loop, then explain why iterating a duplicate subsystem reference would call its method twice.

**Next:** [8. Deploying to Systemcore](../08.2_DeployToSystemcore/deployToSystemcore.md)
