# 5. Running the 2026 Simulator
You can't always have the robot, and even when you do, testing brand new code on it is risky. The **simulator** runs your robot code on your laptop and pretends to be the robot and the Driver Station.

## Goal
By the end you will be able to start the simulator, change the robot's mode, drive with a keyboard or Xbox controller, and watch values on the dashboard.

## Prerequisites
* [4. The Robot Lifecycle](../04_RobotLifecycle/robotLifecycle.md)
* An Xbox controller is nice to have, but you can use the keyboard instead

***
## Step 1. Code that uses a controller
In your `UserChallenges/yourName/` folder, replace `robot.py` with:
```python
import ntcore
import wpilib
import wpilib_drivers


class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.controller = wpilib.Gamepad(0)
        self.motor = wpilib_drivers.PWMSparkMax(0)
        table = ntcore.NetworkTableInstance.get_default().get_table("Tutorial")
        self.speed_publisher = table.get_double_topic("Motor Speed").publish()

    def teleop_periodic(self) -> None:
        speed = -self.controller.get_left_y()
        self.motor.set_throttle(speed)
        self.speed_publisher.set(speed)

    def disabled_init(self) -> None:
        self.motor.set_throttle(0)
```
* `Gamepad(0)` reads the controller plugged into **port 0** of the Driver Station.
* `PWMSparkMax(0)` is a motor controller plugged into **PWM/SmartIO port 0** on the Systemcore. (A simulated PWM motor is the easiest way to see the value change.)
* `motor.set_throttle()` takes a number from **-1.0** (full backward) to **1.0** (full forward).
* **Why the minus sign?** On a controller, pushing the stick **up** gives a **negative** Y value. We flip it so up = forward.
* The publisher writes the number to the `Tutorial/Motor Speed` NetworkTables topic. RobotPy 2026 uses `ntcore` for this direct NetworkTables example.

## Step 2. Start the simulator
In the terminal, inside the folder with `robot.py`:
```
py -3.14 -m robotpy sim
```
The **Robot Simulation** window opens. Here are the parts you'll use most:

| Window | What it's for |
|--------|---------------|
| **Robot State** | Choose **Disconnected**, **Disabled**, **Autonomous**, **Teleoperated** or **Utility**. This is like the Driver Station's enable button. |
| **System Joysticks** | Every controller the laptop can see, plus fake "Keyboard 0-3" controllers |
| **Joysticks** | Ports 0-5, like the Driver Station's USB tab. Your code reads from these. |
| **PWM Outputs** | Shows the value being sent to each PWM motor |
| **NetworkTables** | Shows values published by robot code, including the `Tutorial/Motor Speed` topic |

> Can't find a window? Look in the menus at the top of the simulator window (for example **NetworkTables**, or **Hardware** for PWM Outputs). Drag windows by their title bars to arrange them. The simulator remembers its layout in `simgui.json` and `simgui-window.json`. Those files are in `.gitignore`, so they don't get committed.

## Step 3. Connect a controller
**Keyboard:** drag **Keyboard 0** from **System Joysticks** onto **Joystick[0]** in the **Joysticks** window. To see which keys move which axis, open **DS --> Keyboard 0 Settings**. (Usually **W/S** is axis 1, which is the left stick Y.)

**Xbox controller:** plug it in with USB. It appears in **System Joysticks**. Drag it onto **Joystick[0]**. Check **Map gamepad** so the buttons and axes match a real Xbox controller.

## Step 4. Drive!
1. In **Robot State**, click **Teleoperated**.
1. Push the left stick up and down (or press W/S).
1. Watch **PWM[0]** in **PWM Outputs** and `/Tutorial/Motor Speed` in **NetworkTables** change.
1. Click **Disabled** and push the stick again. `disabled_init` sets the motor command to 0, and WPILib also blocks motor output while the robot is disabled.

## Step 5. Stop the simulator
Close the simulator window, or click in the terminal and press **CTRL-C**.

**Every time you change your code, stop the simulator and start it again.** It does not reload your code automatically.

***
## Common problems
| What you see | What it means |
|--------------|---------------|
| `Warning: Joystick Axis 1 missing (max 0), check if all controllers are plugged in` | Nothing is in **Joystick[0]**. Drag a keyboard or controller there. |
| `Loop time of 0.02s overrun` | Something in a periodic method is too slow. Did someone use `sleep()`? (See Tutorial 4.) |
| `ModuleNotFoundError` for a RobotPy or vendor package | Your laptop is missing a package from `pyproject.toml`. Run `py -3.14 -m robotpy sync` while connected to the internet. |
| `could not find robot.py` or similar | Your terminal is in the wrong folder. `cd` into the folder with `robot.py`. |
| The robot crashes and prints a big red **traceback** | Read it from the **bottom up**. The last line says what went wrong, and the lines above it say which file and line number. |
| The simulator GUI crashes while starting on Linux | Check the desktop/GTK setup. `py -3.14 -m robotpy sim --nogui` can confirm that robot code starts, but it does not provide the simulator windows or controller mapping. |

***
## Challenge
1. Use the **right** stick's Y axis (`get_right_y()`) to control a second motor on port 1. Stop both motors in `disabled_init`.
1. When the **A** button is held (`self.controller.get_face_down_button()`; Xbox A when **Map gamepad** is enabled), scale both motors' commands to **half** speed.
1. Publish a Boolean topic named `A Button` in the `Tutorial` NetworkTables table and set it to the button's current state.
1. Show a mentor or captain all three working in the simulator.

**Next:** [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md)
