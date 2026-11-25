# 8. Deploying 2027 Code to Systemcore
Starting with the 2027 season, FRC robots use a new robot computer called **Systemcore** instead of the roboRIO. This is the 2027 deployment path; the [roboRIO tutorial](../08_DeployToRobot/deployToRobot.md) is only for matching 2026-and-earlier projects.

> ⚠️ **Safety first.** A real robot is heavy, fast and can hurt people. **Only do this tutorial with a mentor or captain present.** Before every enable:
> * The robot is **on blocks** (wheels off the ground), or there is a clear space and a spotter.
> * Everyone near the robot knows it's about to move. Say **"ENABLING!"** loudly.
> * **Before you enable, know how to disable and how to E-Stop in the new Driver Station.** Have a mentor show you, because the keys are not the same as the old Driver Station.

> **Mentor note (written November 2026):** Systemcore, the 2027 Driver Station and RobotPy 2027 were still prerelease software when this was written. Names, addresses and steps may change before kickoff. Check each step against the [WPILib 2027 docs](https://docs.wpilib.org/en/latest/) and [SystemcoreTesting](https://github.com/wpilibsuite/SystemcoreTesting), and use the exact RobotPy version pinned by the team. The example `2027.0.0a8` was tested for the command-line tutorials, but is **not** a recommendation to use that version on the team's robot.

## Goal
By the end you will know what must be ready before a mentor helps you deploy 2027 robot code to a Systemcore and drive it with the FIRST Driver Station.

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
## Part 2. The 2027 API used in these tutorials
Tutorials 3-7 already use the 2027 API, so you do not need to convert your practice project here. Use the exact RobotPy release pinned by the team. When reading older code, remember that the API changed; an old method name may be accepted by Python but never called by WPILib.

| Older RobotPy code | RobotPy 2027 |
|---|---|
| `def robotInit(self):` | `def __init__(self):` and put `super().__init__()` as the **first line** |
| `teleopInit`, `teleopPeriodic`, `teleopExit` | `teleop_init`, `teleop_periodic`, `teleop_exit` |
| `autonomousInit`, `autonomousPeriodic` | `autonomous_init`, `autonomous_periodic` |
| `disabledInit`, `disabledPeriodic` | `disabled_init`, `disabled_periodic` |
| `robotPeriodic` | `robot_periodic` |
| `testInit`, `testPeriodic` | `utility_init`, `utility_periodic` |
| `controller.getLeftY()`, `getAButton()` | `controller.get_left_y()`, `controller.get_face_down_button()` (Xbox A when mapped as a gamepad) |
| `wpilib.XboxController(0)` | These tutorials use `wpilib.Gamepad(0)` |
| `wpilib.PWMSparkMax(0)` | `wpilib_drivers.PWMSparkMax(0)` (need `import wpilib_drivers`) |
| `motor.set(speed)` / `motor.get()` | `motor.set_throttle(speed)` / `motor.get_throttle()` |
| `wpilib.SmartDashboard.putNumber("Name", x)` | Publish a NetworkTables topic with `ntcore`, as in [Tutorial 5](../05_Simulator/simulator.md) |
| `from pyfrc.tests import *` in `tests/` | `from wpilib.testing.robot_tests import *` |

The general rule: **many method names went from `camelCase` to `snake_case`.** RobotPy 2027's `telemetry.log(...)` is a separate telemetry/logging API; it is not the NetworkTables example used in Tutorial 5.

This is the style used for a 2027 robot:
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
```
> On Systemcore, the PWM port number means one of its reconfigurable **SmartIO** ports. The practice code uses a simulated PWM device; it is not a wiring plan for the real robot.

### Update `pyproject.toml`
1. Change `robotpy_version` only if needed so it exactly matches the team's approved 2027 version. This is an example of a prerelease pin, not a team recommendation:
```toml
robotpy_version = "2027.0.0a8"
```
2. Vendor libraries may be configured differently than in older RobotPy projects. Ask a mentor for the exact vendor package names and configuration for this robot; do not copy old `components` or `requires` entries without checking.
3. Run `py -3.14 -m robotpy sync` (with internet).
4. Run `py -3.14 -m robotpy test` and the simulator, and fix everything until they pass.

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
Use a project whose `pyproject.toml` pins the team's approved 2027 RobotPy version.

1. **With internet**, in the folder with `robot.py`:
```
py -3.14 -m robotpy sync
py -3.14 -m robotpy test
```
2. Connect to the Systemcore (Part 4).
3. Deploy:
```
py -3.14 -m robotpy deploy
```
* The first time, it asks `Team number or robot hostname:`. Type `4536`. It looks for the robot at `10.45.36.2`, `robot.local`, and Systemcore's USB and Wi‑Fi addresses, then uses whichever answers.
* It runs the tests. If they fail, it does **not** deploy.
* **The first deploy to a new Systemcore takes several minutes**, because it installs Python and all the packages. Later deploys only take seconds.
* You should see `SUCCESS: Deploy was successful!`

> ⚠️ **Never turn the robot off while a deploy is running.** That can corrupt Systemcore's storage, and then a mentor has to re-image it.

> **Why would it say "roboRIO"?** If any message mentions a roboRIO, check that `robotpy_version` in `pyproject.toml` is the team's 2027 Systemcore version, then run `py -3.14 -m robotpy sync`.

***
## Part 6. Drive and view data
1. Plug in your controller **before** you open the Driver Station if you can. It can send up to 6 controllers to the robot. Make sure yours is in slot **0**.
1. Check that the Driver Station shows it is connected to the robot and that **robot code** is running.
1. Choose **Teleoperated**.
1. Say **"ENABLING!"** and enable. Drive carefully.
1. Disable when you're done.

**E-Stop:** if it is used, stop and ask your mentor to confirm the current reset procedure. Do not attempt to reset it without their direction.

### Where to see robot data
The FIRST Driver Station shows robot connection, mode and controller status. It is **not** a general NetworkTables viewer.

* In simulation, use the simulator's **NetworkTables** window and find the `/Tutorial` table from Tutorial 5.
* On the real robot, use **Glass** (or the NetworkTables dashboard the team uses) to connect to the robot and view topics. Follow the [WPILib Glass connection guide](https://docs.wpilib.org/en/latest/docs/software/dashboards/glass/networktables-connection.html) or ask a mentor to configure it.
* `telemetry.log(...)` is a different 2027 logging API. If team code uses it, view those logs in the team's configured tool, such as AdvantageScope or Elastic.

### Seeing what the robot prints
* The Driver Station has a log window that shows `print()` messages and errors from the robot.
* Or deploy with `py -3.14 -m robotpy deploy --nc` to see the robot's output in the VS Code terminal. This only works while the Driver Station is connected.

***
## Common problems
| What you see | What to try |
|--------------|-------------|
| `Could not find team 4536 robot` | Is Systemcore powered and booted? Are you on its Wi‑Fi or USB-C, not the school Wi‑Fi? Does http://robot.local load? |
| Robot code runs but **nothing happens** in teleop | You still have 2026 names like `teleopPeriodic`. Rename them to snake_case (Part 2). |
| `AttributeError: ... has no attribute 'set'` (or `getLeftY`, etc.) | It's a 2026 name. Use the 2027 name from the Part 2 table. |
| `ModuleNotFoundError: No module named 'pyfrc'` | Your test file is from an older project. For a new 2027 project, use `py -3.14 -m robotpy add-tests` and the generated `tests/robot_test.py`. |
| `ModuleNotFoundError` for a vendor package | Ask a mentor for the correct package and add it to `pyproject.toml`, then run `py -3.14 -m robotpy sync`. |
| The Driver Station can't see the robot | Make sure you are using the **FIRST** Driver Station, not the old NI FRC Driver Station, and that the team number is 4536. |

***
## Challenge
With a mentor or captain watching:
1. Deploy the 2027 controller robot from [Tutorial 5](../05_Simulator/simulator.md), including the second motor and A-button challenge, with a mentor present.
1. Run its tests so `py -3.14 -m robotpy test` passes before deployment.
1. Deploy it to the Systemcore, enable in teleop and drive.
1. Run `py -3.14 -m robotpy deploy-info` and show that **your branch** is the one on the robot.

🎉 **You are ready to start learning autonomous code and planning supervised hardware tests.**
