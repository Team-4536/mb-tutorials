# 4. The Robot Lifecycle: Init, Periodic and Exit
Robot code doesn't run from top to bottom like Hello World. WPILib calls **your** methods at the right moments: when the robot starts, when a match mode starts, and over and over while it's running. In this tutorial you will learn the RobotPy 2027 lifecycle names and when each method runs.

## Goal
By the end you will be able to say exactly when each `Init`, `Periodic` and `Exit` method runs, explain why you must never use `sleep()` in robot code, and find your way around our team's subsystem pattern.

## Prerequisites
* [3. Your First Robot Project](../03_FirstRobotProject/firstRobotProject.md)

***
## The modes
An FRC robot is always in one of these **modes**. The Driver Station (or the simulator) picks the mode.

| Mode | What's happening |
|------|------------------|
| **Disabled** | Robot is on but not allowed to move. This is the mode at power on, before a match and between autonomous and teleop. |
| **Autonomous** | The first 15 seconds of a match (check this season's game manual). The robot drives itself. No controllers. |
| **Teleop** | Teleoperated. The drivers control the robot with controllers. |
| **Utility** | Used in the pits for testing mechanisms. This was called Test in older seasons. |

## The methods
For each mode there are three methods you can write in your `TimedRobot` class:

| Method | When it runs |
|--------|--------------|
| `__init__` | When WPILib creates the robot object; call `super().__init__()` first |
| `robot_periodic` | **Every loop (about 50 times a second), in every mode**, even disabled |
| `disabled_init` / `autonomous_init` / `teleop_init` / `utility_init` | **Once**, every time that mode starts |
| `disabled_periodic` / `autonomous_periodic` / `teleop_periodic` / `utility_periodic` | **Every loop** while in that mode |
| `disabled_exit` / `autonomous_exit` / `teleop_exit` / `utility_exit` | **Once**, every time that mode ends |

You only write the methods you need. If you leave one out, nothing happens at that moment.

### What does a match look like?
```
__init__                    (when WPILib creates the robot object)
disabled_init
disabled_periodic ... x lots   + robot_periodic every loop
disabled_exit
autonomous_init
autonomous_periodic ... x 750  + robot_periodic every loop   (15 seconds x 50 per second)
autonomous_exit
disabled_init
disabled_periodic ... a few    + robot_periodic every loop
disabled_exit
teleop_init
teleop_periodic ... x lots     + robot_periodic every loop
teleop_exit
disabled_init
disabled_periodic ...          (forever until the robot turns off)
```
When a mode changes, WPILib calls the old mode's exit method, then the new mode's init method, then its periodic method over and over. `robot_periodic` also runs every loop in every mode.

***
## Activity A. See it for yourself
1. In your `yourName_robot` folder from Tutorial 3, replace `robot.py` with this:
```python
import wpilib


class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.loops = 0

    def robot_periodic(self) -> None:
        self.loops += 1

    def disabled_init(self) -> None:
        print("disabled_init  loops so far:", self.loops)

    def autonomous_init(self) -> None:
        print("autonomous_init  loops so far:", self.loops)

    def autonomous_exit(self) -> None:
        print("autonomous_exit  loops so far:", self.loops)

    def teleop_init(self) -> None:
        print("teleop_init  loops so far:", self.loops)

    def teleop_periodic(self) -> None:
        if self.loops % 50 == 0:
            print("teleop_periodic is still running... loops:", self.loops)

    def teleop_exit(self) -> None:
        print("teleop_exit  loops so far:", self.loops)
```
2. Run `py -3.14 -m robotpy sim`.
3. In the simulator window, find the **Robot State** box and click **Autonomous**, then **Disabled**, then **Teleoperated**, then **Disabled**.
4. Watch the terminal. Count how many loops happen in about 1 second of teleop.

***
## Never `sleep()` in robot code
Every periodic method has to finish **fast**. It gets 20 milliseconds (0.02 seconds) per loop, and everything has to fit in that time: teleop, `robot_periodic`, all the motors, sensors and dashboard updates.

If you write `time.sleep(1)` inside a periodic method, the **whole robot** freezes for a second. It stops reading the controllers, stops updating the motors, and the terminal fills with loop-overrun warnings. On a real robot that's dangerous.

**What to do instead:** remember things in `self` and check a timer.
```python
# BAD: freezes the robot for 2 seconds
def teleop_periodic(self) -> None:
    self.motor.set_throttle(0.5)
    time.sleep(2)
    self.motor.set_throttle(0)

# GOOD: checks the timer every loop and never waits
def teleop_init(self) -> None:
    self.timer = wpilib.Timer()
    self.timer.restart()

def teleop_periodic(self) -> None:
    if self.timer.get() < 2:
        self.motor.set_throttle(0.5)
    else:
        self.motor.set_throttle(0)
```

***
## How the MinuteBots code is organized: subsystems
A real robot has lots of parts (drive train, intake, shooter, climber, LEDs...). If we put all of that in `robot.py`, it would be thousands of lines long. Instead, each part is a **subsystem** in its own file, and `robot.py` just tells all the subsystems when to run.

The [`RobotCode/robotPeriodicAndInit/src`](../../RobotCode/robotPeriodicAndInit/src) project is a **historical RobotPy 2025 example**. It is useful for reading about the team's old subsystem pattern, but it does not match the 2027 API and should not be synced or run as part of this tutorial.

| File | What it does |
|------|--------------|
| `robot.py` | The `TimedRobot`. It makes the subsystems during startup and calls them from the mode methods. |
| `subsystemManager.py` | Holds every subsystem. `init()`, `periodic()`, `disable()` and `publish()` call that method on **all** the subsystems. |
| `subsystems/subsystem.py` | The blueprint every subsystem follows. Every subsystem must have `init`, `periodic`, `disabled` and `publish`. |
| `subsystems/inputs.py` | Reads the controllers and turns them into a `DesiredState` ("what the drivers want"). |
| `subsystems/desiredState.py` | The "what the drivers want" object that gets passed to every subsystem's `periodic`. |
| `subsystems/myExample.py` | An example subsystem for you to experiment with. |

In that archived project, the team methods line up with the WPILib methods like this. The example uses old camelCase method names; new 2027 projects use snake_case:

| WPILib calls... | ...and our `robot.py` calls |
|-----------------|-----------------------------|
| `teleopInit` | `self.subsystems.init()`, which calls every subsystem's `init()` |
| `teleopPeriodic` | `self.subsystems.periodic()`, which calls every subsystem's `periodic(desiredState)`, then `publish()` |
| `disabledInit` / `disabledPeriodic` | `self.subsystems.disable()`, which calls every subsystem's `disabled()` |

**Rule of thumb for a subsystem:**
* `init`: set things up and reset (set counters to 0, restart timers).
* `periodic`: read the `DesiredState` and decide what the motors should do. Runs every loop.
* `disabled`: make it safe. Stop the motors.
* `publish`: send values to NetworkTables or another dashboard so we can see what's going on.

The archived `pyproject.toml` is pinned to RobotPy 2025 and uses the old `robotpy_extras` setting. Do not change it for this lesson: the team should create a separate 2027 project when this example is updated.

***
## Challenge
1. In your 2027 project, add a counter to `teleop_periodic` and print it only once every 50 loops (hint: `%`).
1. In the archived [`subsystemManager.py`](../../RobotCode/robotPeriodicAndInit/src/subsystemManager.py), find the repeated `self.myExample` entry in `_dependant`. Explain why that subsystem's `periodic` runs twice per manager loop. Treat this as a source-reading exercise only; the project is not runnable with the 2027 toolchain.
1. In your own project, print the final counter once when teleop ends. Use `teleop_exit`, which WPILib calls once per mode transition.

**Next:** [5. Running the Simulator](../05_Simulator/simulator.md)
