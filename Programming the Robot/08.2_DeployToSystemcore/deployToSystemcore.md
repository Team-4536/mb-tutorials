# 8.2 Deploying Code to Systemcore (2027 season)
Starting with the 2027 season, FRC robots use a new robot computer called **Systemcore** instead of the roboRIO. This tutorial is the Systemcore version of [8. Deploying to the Robot](../08_DeployToRobot/deployToRobot.md). It covers getting your code onto a Systemcore and driving with the new **FIRST Driver Station**.

> ⚠️ **Safety first.** A real robot is heavy, fast and can hurt people. **Only do this tutorial with a mentor or captain present.** Before every enable:
> * The robot is **on blocks** (wheels off the ground), or there is a clear space and a spotter.
> * Everyone near the robot knows it's about to move. Say **"ENABLING!"** loudly.
> * **Before you enable, know how to disable and how to E-Stop in the new Driver Station.** Have a mentor show you, because the keys are not the same as the old Driver Station.

> **Mentor note (written November 2026):** Systemcore, the 2027 Driver Station and RobotPy 2027 were all still **alpha/beta** software when this was written (RobotPy `2027.0.0a8`). Names, addresses and steps may change before kickoff. Check each step against the [WPILib 2027 docs](https://docs.wpilib.org/en/latest/) and [SystemcoreTesting](https://github.com/wpilibsuite/SystemcoreTesting) and update this tutorial. Places that most need checking are marked **(check)**.

## Goal
By the end you will be able to update robot code for 2027, deploy it to a Systemcore, and drive it with the FIRST Driver Station.

## Prerequisites
* [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md). Deploy runs the tests first!
* A Windows, Mac or Linux laptop (the new Driver Station runs on all three)
* A Systemcore that a mentor has already **imaged** (installed its operating system) and set to team **4536**

***
## Part 1. What's different from the roboRIO?

| | roboRIO (2026 and earlier) | Systemcore (2027) |
|---|---|---|
| Driver Station | NI **FRC Driver Station**, Windows only | **FIRST Driver Station**, works on Windows, Mac and Linux |
| Connecting from a laptop | USB-B cable, Ethernet, or the robot radio's Wi‑Fi | **USB-C** cable, Ethernet, or Systemcore's **own Wi‑Fi** |
| Address | `roboRIO-4536-FRC.local` | `robot.local` (or `10.45.36.2` on the robot network) |
| Web page | none | `http://robot.local` (the Systemcore dashboard) |
| Modes | Disabled, Autonomous, Teleop, **Test** | Disabled, Autonomous, Teleop, **Utility** (Test was renamed) |
| CAN | 1 CAN bus | Several CAN buses (`can_s0` to `can_s4`) |
| RobotPy version | 2026.x | 2027.x |

**The new Driver Station only works with Systemcore, and the old one only works with the roboRIO.** Make sure you use the right one for the robot in front of you.

***
## Part 2. ⚠️ Your code has to change for 2027
RobotPy 2027 renamed a lot of things. **The biggest trap:** if you leave a method with its old name, Python doesn't give an error. WPILib just **never calls it**, so the robot runs but does nothing. (We tested this. An old-style `teleopPeriodic` in a 2027 project never ran.)

| 2026 (what Tutorials 3-7 show) | 2027 |
|---|---|
| `def robotInit(self):` | `def __init__(self):` and put `super().__init__()` as the **first line** |
| `teleopInit`, `teleopPeriodic`, `teleopExit` | `teleop_init`, `teleop_periodic`, `teleop_exit` |
| `autonomousInit`, `autonomousPeriodic` | `autonomous_init`, `autonomous_periodic` |
| `disabledInit`, `disabledPeriodic` | `disabled_init`, `disabled_periodic` |
| `robotPeriodic` | `robot_periodic` |
| `testInit`, `testPeriodic` | `utility_init`, `utility_periodic` |
| `controller.getLeftY()`, `getAButton()` | `controller.get_left_y()`, `get_a_button()` |
| `wpilib.XboxController(0)` | still works, but `wpilib.Gamepad(0)` works with any gamepad |
| `wpilib.PWMSparkMax(0)` | `wpilib_drivers.PWMSparkMax(0)` (need `import wpilib_drivers`) |
| `motor.set(speed)` / `motor.get()` | `motor.set_throttle(speed)` / `motor.get_throttle()` |
| `wpilib.SmartDashboard.putNumber("Name", x)` | `telemetry.log("Name", x)` (need `import telemetry`) |
| `from pyfrc.tests import *` in `tests/` | `from wpilib.testing.robot_tests import *` |

The general rule: **method names went from `camelCase` to `snake_case`.** If something gives an `AttributeError`, try the snake_case name.

Here's the controller robot from [Tutorial 5](../05_Simulator/simulator.md), updated for 2027:
```python
import telemetry
import wpilib
import wpilib_drivers


class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.controller = wpilib.Gamepad(0)
        self.motor = wpilib_drivers.PWMSparkMax(0)

    def teleop_periodic(self) -> None:
        speed = -self.controller.get_left_y()
        self.motor.set_throttle(speed)
        telemetry.log("Motor Speed", speed)
```
> On Systemcore, the PWM port number means one of its reconfigurable **SmartIO** ports.

### Update `pyproject.toml`
1. Change `robotpy_version` to the team's 2027 version (ask a mentor). For example:
```toml
robotpy_version = "2027.0.0a8"
```
2. Motor and sensor libraries from vendors (REV, CTRE) are **not** in `components` anymore. Put them in `requires` instead. **(check: these were the 2027 package names in November 2026)**
```toml
requires = ["robotpy-rev", "phoenix6"]
```
3. Run `py -m robotpy sync` (with internet).
4. Run `py -m robotpy test` and the simulator, and fix everything until they pass.

***
## Part 3. Install the FIRST Driver Station
1. Download the newest release from [github.com/wpilibsuite/FirstDriverStation-Public/releases](https://github.com/wpilibsuite/FirstDriverStation-Public/releases/latest).
   * **Windows:** the `.exe`. Run it to install.
   * **Mac:** the `.pkg`. The first time it runs, allow **Input Monitoring** and **Local Network** in System Settings, then quit and reopen it.
   * **Linux:** ask a mentor. It needs extra setup (an `input` group and a udev rule).
2. Open it and set the team number to **4536** **(check: where this setting is)**.
3. Every time the Driver Station starts, it asks you to do a quick keyboard check. That check is part of the safety system, so don't skip it.

***
## Part 4. Connect to the Systemcore
Power on the robot and wait for Systemcore to finish booting. Its **display** shows its addresses and Wi‑Fi info when it's ready. Then connect **one** of these ways:

| Connection | How | Good for |
|------------|-----|----------|
| **USB-C** | USB-C cable from the laptop to Systemcore | Bench work. Easiest. |
| **Systemcore Wi‑Fi** | Join the network named `SYSTEMCORE-...`. **The password is shown on Systemcore's display.** | Driving around. **No internet** while connected! |
| **Ethernet** | Network cable to Systemcore's Ethernet port (the address is shown on the display) | In the pits |

### Check the connection
Open a web browser and go to **http://robot.local**. You should see the **Systemcore dashboard**. If it loads, you're connected. (Mentors also use this page to update Systemcore and set the team number.)

> If `robot.local` doesn't load, try the Wi‑Fi address `http://172.30.0.1`, or the address on Systemcore's display.

***
## Part 5. Deploy
Same as the roboRIO, just make sure you're on the 2027 project.

1. **With internet**, in the folder with `robot.py`:
```
py -m robotpy sync
py -m robotpy test
```
2. Connect to the Systemcore (Part 4).
3. Deploy:
```
py -m robotpy deploy
```
* The first time, it asks `Team number or robot hostname:`. Type `4536`. It looks for the robot at `10.45.36.2`, `robot.local`, and Systemcore's USB and Wi‑Fi addresses, then uses whichever answers.
* It runs the tests. If they fail, it does **not** deploy.
* **The first deploy to a new Systemcore takes several minutes**, because it installs Python and all the packages. Later deploys only take seconds.
* You should see `SUCCESS: Deploy was successful!`

> ⚠️ **Never turn the robot off while a deploy is running.** That can corrupt Systemcore's storage, and then a mentor has to re-image it.

> **Why would it say "roboRIO"?** If any message mentions a roboRIO, you're using RobotPy 2026. Check `robotpy_version` in `pyproject.toml` and run `py -m robotpy sync`.

***
## Part 6. Drive with the FIRST Driver Station
1. Plug in your controller **before** you open the Driver Station if you can. It can send up to 6 controllers to the robot. Make sure yours is in slot **0**.
1. Check that the Driver Station shows it is connected to the robot and that **robot code** is running.
1. Choose **Teleoperated**.
1. Say **"ENABLING!"** and enable. Drive carefully.
1. Disable when you're done.

**E-Stop:** if the E-Stop is used, the robot locks out. To reset it, hold **Escape** and **I** together for 1 second **(check: this may change)**.

### Seeing what the robot prints
* The Driver Station has a log window that shows `print()` messages and errors from the robot.
* Or deploy with `py -m robotpy deploy --nc` to see the robot's output in the VS Code terminal. This only works while the Driver Station is connected.
* Values you send with `telemetry.log(...)` can be viewed in **AdvantageScope** or **Elastic**. Mentors can install those from the Systemcore dashboard.

***
## Common problems
| What you see | What to try |
|--------------|-------------|
| `Could not find team 4536 robot` | Is Systemcore powered and booted? Are you on its Wi‑Fi or USB-C, not the school Wi‑Fi? Does http://robot.local load? |
| Robot code runs but **nothing happens** in teleop | You still have 2026 names like `teleopPeriodic`. Rename them to snake_case (Part 2). |
| `AttributeError: ... has no attribute 'set'` (or `getLeftY`, etc.) | It's a 2026 name. Use the 2027 name from the Part 2 table. |
| `ModuleNotFoundError: No module named 'pyfrc'` | Your `tests/` file is from 2026. Change it to `from wpilib.testing.robot_tests import *`. |
| `ModuleNotFoundError` for `rev`, `phoenix6`, etc. | Add the vendor package to `requires` in `pyproject.toml` and run `py -m robotpy sync`. |
| The Driver Station can't see the robot | Make sure you are using the **FIRST** Driver Station, not the old NI FRC Driver Station, and that the team number is 4536. |

***
## Challenge
With a mentor or captain watching:
1. Convert your controller robot from [Tutorial 5](../05_Simulator/simulator.md) to 2027 (Part 2), including the challenge parts (second motor, A button for half speed, A-button value with `telemetry.log`).
1. Update its tests so `py -m robotpy test` passes.
1. Deploy it to the Systemcore, enable in teleop and drive.
1. Run `py -m robotpy deploy-info` and show that **your branch** is the one on the robot.

🎉 **You're ready for the 2027 robot!**
