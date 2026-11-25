# 7. Debugging Robot Code
The [debugger tutorial](../../debugger%20tutorial.md) showed you breakpoints and stepping through a normal Python file. Robot code is a little different: you don't run `robot.py` directly, you run `robotpy sim`. In this tutorial you will set up VS Code so the debugger can pause robot code while the simulator is running.

## Goal
By the end you will be able to press **F5** to start the simulator in the debugger, stop on a breakpoint inside `teleopPeriodic`, look at variables, and debug a test.

## Prerequisites
* [debugger tutorial](../../debugger%20tutorial.md) (how breakpoints, step over, step into and continue work)
* [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md)
* The **Python** extension from Microsoft installed in VS Code (from [Tutorial 1](../01_LaptopSetup/laptopSetup.md))

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
* `"module": "robotpy"` and `"args": ["sim"]` mean "run `py -m robotpy sim`", the same command you've been typing.
* `"cwd": "${fileDirname}"` means "run it in the folder of the file I have open right now". **So open `robot.py` (click on its tab) before you press F5.**
* `"--no-isolation"` makes the tests run inside the debugger. Normally each test runs in its own separate process, and the debugger can't see into those.
* `"justMyCode": true` means "only stop in our code, not inside WPILib".

> If the robot repo already has a `.vscode/launch.json`, just add these two configurations to its `"configurations"` list.

***
## Step 2. Set a breakpoint and start debugging
Use the controller robot from [Tutorial 5](../05_Simulator/simulator.md).

1. Open `robot.py`. Click to the left of the line number on `self.motor.set(speed)` so a **red dot** appears.
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
## Using the debugger on team code
In the sample project, [`RobotCode/robotPeriodicAndInit/src`](../../RobotCode/robotPeriodicAndInit/src):
1. Open `subsystemManager.py` and put a breakpoint inside `periodic` on the line `s.periodic(ds)`.
1. Open `robot.py`, choose **RobotPy: Simulate** and press F5. Switch to **Teleoperated**.
1. Use **Step Into** (F11) to follow the code into each subsystem's `periodic`. Watch the `s` variable change as the loop goes through the subsystems.

***
## Challenge
In the sample project, use **only the debugger** (no `print`s!) to prove which subsystem gets its `periodic` called **twice** every loop. Show a mentor or captain the breakpoint and the Variables panel that proves it.

**Next:** [8. Deploying to the Robot](../08_DeployToRobot/deployToRobot.md)
