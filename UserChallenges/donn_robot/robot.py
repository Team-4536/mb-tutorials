# import ntcore
# import wpilib

# class MyRobot(wpilib.TimedRobot):
#     def __init__(self) -> None:
#         super().__init__()
#         self.timer = wpilib.Timer()
#         table = ntcore.NetworkTableInstance.getDefault().getTable("Tutorial")
#         self.teleop_seconds = table.getDoubleTopic("Teleop Seconds").publish()
#         self.teleop_operator = table.getStringTopic("Teleop Operator").publish()

#     def teleopInit(self) -> None:
#         self.teleop_operator.set("Coach Donn")
#         print("Teleop started by Coach Donn")
#         self.timer.restart()

#     def teleopPeriodic(self) -> None:
#         self.teleop_seconds.set(self.timer.get())
        
#     def teleopExit(self) -> None:
#         self.teleop_operator.set("N/A")
#         print("Teleop ended by Coach Donn")


import wpilib


class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
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
