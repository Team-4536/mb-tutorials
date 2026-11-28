import ntcore
import wpilib

class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.timer = wpilib.Timer()
        table = ntcore.NetworkTableInstance.getDefault().getTable("Tutorial")
        self.teleop_seconds = table.getDoubleTopic("Teleop Seconds").publish()
        self.teleop_operator = table.getStringTopic("Teleop Operator").publish()

    def teleopInit(self) -> None:
        self.teleop_operator.set("Coach Donn")
        print("Teleop started by Coach Donn")
        self.timer.restart()

    def teleopPeriodic(self) -> None:
        self.teleop_seconds.set(self.timer.get())
        
    def teleopExit(self) -> None:
        self.teleop_operator.set("N/A")
        print("Teleop ended by Coach Donn")