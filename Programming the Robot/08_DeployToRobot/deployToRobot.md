# 8. Deploying Code to the Robot
**Deploying** means copying your code onto the robot's computer (the **roboRIO**) and starting it. Then you use the **FRC Driver Station** to enable the robot and drive it.

> ⚠️ **Safety first.** A real robot is heavy, fast and can hurt people. **Only do this tutorial with a mentor or captain present.** Before every enable:
> * The robot is **on blocks** (wheels off the ground), or there is a clear space and a spotter.
> * Everyone near the robot knows it's about to move. Say **"ENABLING!"** loudly.
> * Your hand is ready to disable: **Enter** disables the robot, **Space bar** is the emergency stop. (After an emergency stop, the robot has to be rebooted.)

> **Using a Systemcore (2027)?** This tutorial is for the **roboRIO** with RobotPy 2026. For Systemcore, use [8.2 Deploying to Systemcore](../08.2_DeployToSystemcore/deployToSystemcore.md) instead.

## Goal
By the end you will have deployed code to the robot, enabled it from the Driver Station, driven it, and seen its printed messages.

## Prerequisites
* [6. Testing Robot Code](../06_TestingRobotCode/testingRobotCode.md). Deploy runs the tests first!
* A Windows laptop with the **FRC Driver Station** installed ([Tutorial 1, Step 6](../01_LaptopSetup/laptopSetup.md))
* A robot (or just a roboRIO on the bench) that has a mentor's OK

***
## Step 1. Before you leave the internet: `sync`
The robot has **no internet**, so the laptop has to download everything the robot needs **first**, while it's still on the MinuteBots wifi. In the folder with `robot.py`:
```
py -m robotpy sync
```
Run it again whenever `pyproject.toml` changes (a new RobotPy version, or a new component like `rev` or `phoenix6`).

## Step 2. Make sure the tests pass
```
py -m robotpy test
```
Deploy runs these anyway. It's faster to find problems here.

***
## Step 3. Connect to the robot
Turn the robot on and wait about 30 seconds for the roboRIO to boot (the **RIO** status light stops blinking). Then connect **one** of these ways:

| Connection | How | Good for |
|------------|-----|----------|
| **USB** | USB cable from the laptop to the roboRIO's USB **device** port (the square-ish USB-B port) | Bench work. Easiest and most reliable. |
| **Ethernet** | Network cable from the laptop to the robot's radio | In the pits |
| **Wifi** | Connect to the robot's wifi network (it has **4536** in the name, ask for the password) | Driving around. **No internet** while connected! |

Our team number is **4536**, so the tools look for the robot at `roboRIO-4536-FRC.local` (or `10.45.36.2`).

***
## Step 4. Deploy
```
py -m robotpy deploy
```
* **The first time** in a project, it asks `Team number or robot hostname:`. Type `4536`. It saves the answer in `.wpilib/wpilib_preferences.json` (the sample project already has this file).
* It runs the tests. If any fail, **it stops and does not deploy**. Fix the code!
* It checks Python and the packages on the roboRIO, and installs anything missing from `pyproject.toml`. **This can take several minutes the first time** after a roboRIO is set up or the RobotPy version changes. After that it only takes a few seconds.
* It copies your code and restarts the robot program.

When it finishes, you'll see something like `SUCCESS: Deploy was successful!`

> **Never use `--skip-tests` to "fix" a failed deploy.** The tests are failing because your code crashes. If it crashes on the robot, the robot stops working mid-match.

***
## Step 5. Drive with the Driver Station
1. Open **FRC Driver Station**.
1. Click the **gear (Setup)** tab on the left and make sure **Team Number** is `4536`.
1. Look at the three lights in the middle:
   * **Communications**: is the laptop talking to the robot?
   * **Robot Code**: is our code running?
   * **Joysticks**: is a controller plugged in?

   All three must be **green**.
1. Plug in the Xbox controller. On the **USB** tab (the icon that looks like a USB plug), make sure it is in slot **0**. Drag it there if it isn't.
1. On the **Operation** tab (the steering wheel icon), choose **TeleOperated**.
1. Say **"ENABLING!"** and click **Enable**. Drive carefully.
1. Click **Disable** (or press **Enter**) when you're done.

***
## Step 6. See what the robot prints
`print()` messages from the robot show up in the Driver Station's message window. To also see them in the VS Code terminal, deploy with:
```
py -m robotpy deploy --nc
```
`--nc` (NetConsole) keeps showing the robot's output after deploying. Press **CTRL-C** to stop watching. That doesn't stop the robot.

***
## Other useful commands
| Command | What it does |
|---------|--------------|
| `py -m robotpy deploy-info` | Shows what code is on the robot: which laptop user deployed it, when, and from which git branch/commit |
| `py -m robotpy undeploy` | Removes our Python code from the robot |
| `py -m robotpy deploy --skip-tests` | Deploys without testing. **Mentor approval only.** |

## Common problems
| What you see | What to try |
|--------------|-------------|
| Can't find / connect to `roboRIO-4536-FRC.local` | Is the robot on and booted? Are you connected to the robot (USB/ethernet/robot wifi), not the school wifi? Try USB. |
| Errors about missing packages, or `sync` | You skipped Step 1 or `pyproject.toml` changed. Get back on the internet and run `py -m robotpy sync`. |
| **Robot Code** light is red after deploying | Our code crashed on the robot. Read the Driver Station messages (or deploy with `--nc`) and look for a traceback. |
| **Joysticks** light is red | Plug the controller in, then check the USB tab. |
| Robot enables but nothing moves | Is the controller in USB slot 0? Are you in TeleOperated? Do the motor CAN IDs/ports in the code match the robot? |

***
## Challenge
With a mentor or captain watching:
1. Deploy the controller robot from [Tutorial 5](../05_Simulator/simulator.md) (or this season's robot code from your branch).
1. Enable in teleop and drive.
1. Run `py -m robotpy deploy-info` and show that **your branch** is the one on the robot.

🎉 **You're done with Programming the Robot!** Next, find a robot code issue on GitHub and assign yourself to it (see the [using GitHub tutorial](../../using%20GitHub%20tutorial.md)).
