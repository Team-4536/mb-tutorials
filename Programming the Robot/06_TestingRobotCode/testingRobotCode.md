# 6. Testing 2027 Robot Code
A **test** is code that checks your other code automatically. RobotPy can start your robot, run it through autonomous and teleop super fast (no waiting for real time) and tell you if it crashed. **`robotpy deploy` runs the tests before it puts code on the robot, and it won't deploy if a test fails.** That's why you need to know this before Tutorial 8.

## Goal
By the end you will be able to run the built-in robot tests, read the results, and write a simple test of your own.

## Prerequisites
* [5. Running the Simulator](../05_Simulator/simulator.md)

***
## Step 1. Add the built-in tests
In your `yourName_robot` folder:
```
py -3.14 -m robotpy add-tests
```
For RobotPy 2027, this creates `tests/robot_test.py`. It imports the basic tests supplied by WPILib:
```python
from wpilib.testing.robot_tests import *
```
These tests exercise common robot modes and check that the robot code starts and runs without crashing. The exact test names and number may vary with the pinned RobotPy release.

## Step 2. Run the tests
```
py -3.14 -m robotpy test
```
When everything works, the end of the output has a pytest summary with no failures. A test may be marked **skipped** by the framework:
```
============================== 4 passed, 1 skipped ==============================
```
Each `.` is a test that passed. A failed test shows an **F**, along with a report about what went wrong. Like any traceback, read it from the bottom up.

> For the tested RobotPy `2027.0.0a8` prerelease, the generated tests produced 4 passes and 1 skip. Your mentor-pinned release may report a different count.

## Step 3. Break it on purpose
1. In `teleop_periodic`, add a line that will crash, like `print(10 / 0)`.
1. Run `py -3.14 -m robotpy test` again. Which tests fail? Find `ZeroDivisionError` and the line number in the output.
1. Remove the bad line and make sure all runnable tests pass again.

***
## Step 4. Write your own test
Built-in tests only check that the robot doesn't **crash**. Your own tests can check that it does the **right thing**.

Create a new file: `tests/teleop_test.py`. (Test files must end in `_test.py` or start with `test_`, and test functions must start with `test_`.)

This test goes with the timer robot from [Tutorial 3](../03_FirstRobotProject/firstRobotProject.md):
```python
def test_teleop_timer_counts_up(control, robot):
    with control.run_robot():
        control.step_timing(seconds=2, autonomous=False, enabled=True)
        assert robot.timer.get() > 1
```
What it does:
* `control` and `robot` are given to you by RobotPy. `robot` is **your** `MyRobot` object, so you can look at anything you stored in `self`.
* `control.run_robot()` starts the robot code.
* `control.step_timing(...)` runs the robot for 2 seconds of **pretend** time in teleop, enabled. (It takes way less than 2 real seconds.)
* `assert` means "this had better be true, or the test fails".

Run `py -3.14 -m robotpy test` and confirm the new test passes.

***
## Historical team example
[`RobotCode/robotPeriodicAndInit/src/conftest.py`](../../RobotCode/robotPeriodicAndInit/src/conftest.py) belongs to the archived RobotPy 2025 project and imports `pyfrc`. Do not run that project with the 2027 tutorial setup. A current 2027 team project may have its own `conftest.py`; follow that project's instructions.

***
## Challenge
Use the controller robot from [Tutorial 5](../05_Simulator/simulator.md) for this one.

1. Make sure `py -3.14 -m robotpy test` passes for it.
1. Write a test that checks the motor command is **zero** after the robot is disabled. Use the 2027 motor API (`get_throttle()`), and make sure your test first sets it to a nonzero value:
   ```python
   def test_motor_stops_when_disabled(control, robot):
       with control.run_robot():
           robot.motor.set_throttle(0.5)
           control.step_timing(seconds=1, autonomous=False, enabled=False)
           assert robot.motor.get_throttle() == 0
   ```
   This passes because the Tutorial 5 robot explicitly sets the motor to zero in `disabled_init`. WPILib blocks hardware output while disabled, but a motor controller's getter can still report its last commanded setpoint unless your code clears it.
1. Explain why the archived example's `sleep(1)` in a periodic method makes it unsuitable for fast automated tests. Do not run the archived 2025 project as part of this 2027 workflow.

**Next:** [7. Debugging Robot Code](../07_DebuggingRobotCode/debuggingRobotCode.md)
