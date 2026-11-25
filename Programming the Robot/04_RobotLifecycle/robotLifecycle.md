# 4. The Robot Lifecycle: Init, Periodic and Exit
Robot code doesn't run from top to bottom like Hello World. WPILib calls **your** methods at the right moments: when the robot turns on, when a match mode starts, and over and over while it's running. In this tutorial you will learn when each method runs.

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
| **Test** | Used in the pits for testing mechanisms. Never used in a match. |

## The methods
For each mode there are three methods you can write in your `TimedRobot` class:

| Method | When it runs |
|--------|--------------|
| `robotInit` | **Once**, when the robot code starts |
| `robotPeriodic` | **Every loop (50 times a second), in every mode**, even disabled |
| `disabledInit` / `autonomousInit` / `teleopInit` / `testInit` | **Once**, every time that mode starts |
| `disabledPeriodic` / `autonomousPeriodic` / `teleopPeriodic` / `testPeriodic` | **Every loop** while in that mode |
| `disabledExit` / `autonomousExit` / `teleopExit` / `testExit` | **Once**, every time that mode ends |

You only write the methods you need. If you leave one out, nothing happens at that moment.

### What does a match look like?
```
robotInit                  (once, when the robot turns on)
disabledInit
disabledPeriodic ... x lots   + robotPeriodic every loop
disabledExit
autonomousInit
autonomousPeriodic ... x 750  + robotPeriodic every loop   (15 seconds x 50 per second)
autonomousExit
disabledInit
disabledPeriodic ... a few    + robotPeriodic every loop
disabledExit
teleopInit
teleopPeriodic ... x lots     + robotPeriodic every loop
teleopExit
disabledInit
disabledPeriodic ...          (forever until the robot turns off)
```
Every time the mode changes, the old mode's **Exit** runs, then the new mode's **Init**, then its **Periodic** over and over.

> **Where does `robotPeriodic` go in a loop?** Every 20 milliseconds WPILib calls the mode's periodic method (like `teleopPeriodic`) **first**, then `robotPeriodic`.

***
## Activity A. See it for yourself
1. In your `yourName_robot` folder from Tutorial 3, replace `robot.py` with this:
```python
import wpilib


class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        print("robotInit")
        self.loops = 0

    def robotPeriodic(self) -> None:
        self.loops += 1

    def disabledInit(self) -> None:
        print("disabledInit  loops so far:", self.loops)

    def autonomousInit(self) -> None:
        print("autonomousInit  loops so far:", self.loops)

    def autonomousExit(self) -> None:
        print("autonomousExit  loops so far:", self.loops)

    def teleopInit(self) -> None:
        print("teleopInit  loops so far:", self.loops)

    def teleopPeriodic(self) -> None:
        if self.loops % 50 == 0:
            print("teleopPeriodic is still running... loops:", self.loops)

    def teleopExit(self) -> None:
        print("teleopExit  loops so far:", self.loops)
```
2. Run `py -m robotpy sim`.
3. In the simulator window, find the **Robot State** box and click **Autonomous**, then **Disabled**, then **Teleoperated**, then **Disabled**.
4. Watch the terminal. Count how many loops happen in about 1 second of teleop.

***
## Never `sleep()` in robot code
Every periodic method has to finish **fast**. It gets 20 milliseconds (0.02 seconds) per loop, and everything has to fit in that time: teleop, robotPeriodic, all the motors, sensors and dashboard updates.

If you write `time.sleep(1)` inside a periodic method, the **whole robot** freezes for a second. It stops reading the controllers, stops updating the motors, and the terminal fills with `Loop time of 0.02s overrun` warnings. On a real robot that's dangerous.

**What to do instead:** remember things in `self` and check a timer.
```python
# BAD: freezes the robot for 2 seconds
def teleopPeriodic(self) -> None:
    self.motor.set(0.5)
    time.sleep(2)
    self.motor.set(0)

# GOOD: checks the timer every loop and never waits
def teleopInit(self) -> None:
    self.timer = wpilib.Timer()
    self.timer.restart()

def teleopPeriodic(self) -> None:
    if self.timer.get() < 2:
        self.motor.set(0.5)
    else:
        self.motor.set(0)
```

***
## How the MinuteBots code is organized: subsystems
A real robot has lots of parts (drive train, intake, shooter, climber, LEDs...). If we put all of that in `robot.py`, it would be thousands of lines long. Instead, each part is a **subsystem** in its own file, and `robot.py` just tells all the subsystems when to run.

Open the example project in this repo: [`RobotCode/robotPeriodicAndInit/src`](../../RobotCode/robotPeriodicAndInit/src).

| File | What it does |
|------|--------------|
| `robot.py` | The `TimedRobot`. It makes the subsystems in `robotInit` and calls them from the mode methods. |
| `subsystemManager.py` | Holds every subsystem. `init()`, `periodic()`, `disable()` and `publish()` call that method on **all** the subsystems. |
| `subsystems/subsystem.py` | The blueprint every subsystem follows. Every subsystem must have `init`, `periodic`, `disabled` and `publish`. |
| `subsystems/inputs.py` | Reads the controllers and turns them into a `DesiredState` ("what the drivers want"). |
| `subsystems/desiredState.py` | The "what the drivers want" object that gets passed to every subsystem's `periodic`. |
| `subsystems/myExample.py` | An example subsystem for you to experiment with. |

Here's how the team methods line up with the WPILib methods in `robot.py`:

| WPILib calls... | ...and our `robot.py` calls |
|-----------------|-----------------------------|
| `teleopInit` | `self.subsystems.init()`, which calls every subsystem's `init()` |
| `teleopPeriodic` | `self.subsystems.periodic()`, which calls every subsystem's `periodic(desiredState)`, then `publish()` |
| `disabledInit` / `disabledPeriodic` | `self.subsystems.disable()`, which calls every subsystem's `disabled()` |

**Rule of thumb for a subsystem:**
* `init`: set things up and reset (set counters to 0, restart timers).
* `periodic`: read the `DesiredState` and decide what the motors should do. Runs every loop.
* `disabled`: make it safe. Stop the motors.
* `publish`: send values to NetworkTables/the dashboard so we can see what's going on.

***
## Activity B. Run the example
1. Open a terminal and `cd` into the example:
```
cd RobotCode/robotPeriodicAndInit/src
```
2. Open `pyproject.toml`. If `robotpy_version` is older than the version the team is using this season, change it to match (ask a mentor). In newer RobotPy versions the list is called `components` instead of `robotpy_extras`. If you change anything, run `py -m robotpy sync`.
3. Run `py -m robotpy sim` and switch the Robot State to **Teleoperated**.

You'll see `this runs once`, then `this will run forever`... **slowly**, along with loop overrun warnings. That's because `myExample.py` has a `sleep(1)` in `periodic`!

> You will also see `Warning: Joystick Axis ... missing` messages. Those are normal in the simulator when no controller is connected. You'll fix that in the next tutorial.

***
## Challenge
1. In `subsystems/myExample.py`, delete the `sleep(1)` (and the `from time import sleep` line). Use the commented-out `self.myCounter` lines instead, so `periodic` counts loops. Change it so it only prints once every 50 loops (hint: `%`).
1. Run the sim in teleop for about 5 seconds. **Is the counter going up twice as fast as you expected?** Find out why. (Hint: look closely at the `_dependant` list in `subsystemManager.py`.) Tell a mentor what you found and how you would fix it.
1. Change the `disabled` method in `MyExample` so it prints the final count, but only **once** each time the robot is disabled. Be careful about two things:
   * Our `robot.py` calls `disabled()` **every loop** while disabled, not just once.
   * The robot starts out disabled, **before** `init` has ever run, so `self.myCounter` doesn't exist yet. (Hint: set it up in `__init__` too.)

**Next:** [5. Running the Simulator](../05_Simulator/simulator.md)
