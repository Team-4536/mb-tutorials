# 6. Testing Robot Code
A **test** is code that checks your other code automatically. RobotPy can start your robot, run it through autonomous and teleop super fast (no waiting for real time) and tell you if it crashed. **`robotpy deploy` runs the tests before it puts code on the robot, and it won't deploy if a test fails.** That's why you need to know this before Tutorial 8.

## Goal
By the end you will be able to run the built-in robot tests, read the results, and write a simple test of your own.

## Prerequisites
* [5. Running the Simulator](../05_Simulator/simulator.md)

***
## Step 1. Add the built-in tests
In your `yourName_robot` folder:
```
py -m robotpy add-tests
```
This creates `tests/pyfrc_test.py`. It's only one line:
```python
from pyfrc.tests import *
```
That line brings in 4 ready-made tests that work for just about any robot:

| Test | What it checks |
|------|----------------|
| `test_disabled` | The robot starts up and runs while disabled without crashing |
| `test_autonomous` | It runs a whole autonomous period without crashing |
| `test_operator_control` | It runs teleop without crashing |
| `test_practice` | It runs a full practice match (disabled, auto, disabled, teleop) without crashing |

## Step 2. Run the tests
```
py -m robotpy test
```
When everything works, the end of the output looks like this:
```
tests/pyfrc_test.py ....                                                 [100%]
============================== 4 passed in 1.17s ===============================
```
Each `.` is a test that passed. A failed test shows an **F**, along with a long report about what went wrong. Like any traceback, read it from the bottom up.

> Another way to get these tests without making a `tests` folder is `py -m robotpy test --builtin`.

## Step 3. Break it on purpose
1. In `teleopPeriodic`, add a line that will crash, like `print(10 / 0)`.
1. Run `py -m robotpy test` again. Which tests fail? Find `ZeroDivisionError` and the line number in the output.
1. Remove the bad line and make sure all 4 pass again.

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

Run `py -m robotpy test` and look for `tests/teleop_test.py .`

***
## Team code: `conftest.py`
Open [`RobotCode/robotPeriodicAndInit/src/conftest.py`](../../RobotCode/robotPeriodicAndInit/src/conftest.py). `conftest.py` is a special pytest file that sets up tests. Ours tells the test system which robot class to use (`Robot` from `robot.py`). You usually don't need to change it.

***
## Challenge
Use the controller robot from [Tutorial 5](../05_Simulator/simulator.md) for this one.

1. Make sure `py -m robotpy test` passes for it.
1. Write a test that checks the motor is **stopped** (`robot.motor.get() == 0`) after running for 1 second with `enabled=False`.
1. **Bonus:** in the sample project (`RobotCode/robotPeriodicAndInit/src`), run `py -m robotpy test --builtin`. Does it finish? If it seems stuck, think about what `sleep(1)` does when the tests run thousands of loops. (Press **CTRL-C** to stop it.)

**Next:** [7. Debugging Robot Code](../07_DebuggingRobotCode/debuggingRobotCode.md)
