import ntcore
import wpilib

class MyRobot(wpilib.TimedRobot):
    def __init__(self) -> None:
        super().__init__()
        self.timer = wpilib.Timer()
        table = ntcore.NetworkTableInstance.get_default().get_table("Tutorial")
        self.teleop_seconds = table.get_double_topic("Teleop Seconds").publish()

    def teleop_init(self) -> None:
        print("Teleop started")
        self.timer.restart()

    def teleop_periodic(self) -> None:
        self.teleop_seconds.set(self.timer.get())