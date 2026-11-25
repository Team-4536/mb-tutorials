# 5. Running the Simulator
You can't always have the robot, and even when you do, testing brand new code on it is risky. The **simulator** runs your robot code on your laptop and pretends to be the robot and the Driver Station.

## Goal
By the end you will be able to start the simulator, change the robot's mode, drive with a keyboard or Xbox controller, and watch values on the dashboard.

## Prerequisites
* [4. The Robot Lifecycle](../04_RobotLifecycle/robotLifecycle.md)
* An Xbox controller is nice to have, but you can use the keyboard instead

***
## Step 1. Code that uses a controller
In your `yourName_robot` folder, replace `robot.py` with:
```python
import wpilib


class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.controller = wpilib.XboxController(0)
        self.motor = wpilib.PWMSparkMax(0)

    def teleopPeriodic(self) -> None:
        speed = -self.controller.getLeftY()
        self.motor.set(speed)
        wpilib.SmartDashboard.putNumber("Motor Speed", speed)
```
* `XboxController(0)` is the controller plugged into **port 0** of the Driver Station.
* `PWMSparkMax(0)` is a motor controller plugged into **PWM port 0** on the robot. (Our real robot uses CAN motor controllers, but a PWM motor is the easiest to see in the simulator.)
* `motor.set()` takes a number from **-1.0** (full backward) to **1.0** (full forward).
* **Why the minus sign?** On a controller, pushing the stick **up** gives a **negative** Y value. We flip it so up = forward.

## Step 2. Start the simulator
In the terminal, inside the folder with `robot.py`:
```
py -m robotpy sim
```
The **Robot Simulation** window opens. Here are the parts you'll use most:

| Window | What it's for |
|--------|---------------|
| **Robot State** | Choose **Disconnected**, **Disabled**, **Autonomous**, **Teleoperated** or **Test**. This is like the Driver Station's enable button. |
| **System Joysticks** | Every controller the laptop can see, plus fake "Keyboard 0-3" controllers |
| **Joysticks** | Ports 0-5, like the Driver Station's USB tab. Your code reads from these. |
| **PWM Outputs** | Shows the value being sent to each PWM motor |
| **NetworkTables** | Shows everything sent to the dashboard (like `SmartDashboard`) |

> Can't find a window? Look in the menus at the top of the simulator window (for example **NetworkTables**, or **Hardware** for PWM Outputs). Drag windows by their title bars to arrange them. The simulator remembers your layout in `simgui.json` and `simgui-window.json`. Those files are in `.gitignore`, so they don't get committed.

## Step 3. Connect a controller
**Keyboard:** drag **Keyboard 0** from **System Joysticks** onto **Joystick[0]** in the **Joysticks** window. To see which keys move which axis, open **DS --> Keyboard 0 Settings**. (Usually **W/S** is axis 1, which is the left stick Y.)

**Xbox controller:** plug it in with USB. It appears in **System Joysticks**. Drag it onto **Joystick[0]**. Check **Map gamepad** so the buttons and axes match a real Xbox controller.

## Step 4. Drive!
1. In **Robot State**, click **Teleoperated**.
1. Push the left stick up and down (or press W/S).
1. Watch **PWM[0]** in **PWM Outputs** and **Motor Speed** in **NetworkTables --> SmartDashboard** change.
1. Click **Disabled** and push the stick again. The motor goes to 0, because WPILib automatically stops every motor when the robot is disabled.

## Step 5. Stop the simulator
Close the simulator window, or click in the terminal and press **CTRL-C**.

**Every time you change your code, stop the simulator and start it again.** It does not reload your code automatically.

***
## Common problems
| What you see | What it means |
|--------------|---------------|
| `Warning: Joystick Axis 1 missing (max 0), check if all controllers are plugged in` | Nothing is in **Joystick[0]**. Drag a keyboard or controller there. |
| `Loop time of 0.02s overrun` | Something in a periodic method is too slow. Did someone use `sleep()`? (See Tutorial 4.) |
| `ModuleNotFoundError: No module named 'rev'` (or another package) | Your laptop is missing a package from `pyproject.toml`. Run `py -m robotpy sync`. |
| `could not find robot.py` or similar | Your terminal is in the wrong folder. `cd` into the folder with `robot.py`. |
| The robot crashes and prints a big red **traceback** | Read it from the **bottom up**. The last line says what went wrong, and the lines above it say which file and line number. |

***
## Challenge
1. Use the **right** stick's Y axis (`getRightY()`) to control a second motor on PWM port 1.
1. When the **A** button is held (`self.controller.getAButton()`), make both motors go at **half** speed.
1. Put a `True`/`False` on the dashboard that shows whether A is pressed (`wpilib.SmartDashboard.putBoolean`).
1. Show a mentor or captain all three working in the simulator.

**Next:** [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md)
