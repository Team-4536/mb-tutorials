from subsystems.desiredState import DesiredState
from subsystems.subsystem import Subsystem
from time import sleep


class MyExample(Subsystem):


    def init(self) -> None:
        print("this runs once")
        # self.myCounter = 1

    def periodic(self, ds: DesiredState) -> None:
        print("this will run forever")
        # self.myCounter += 1
        # print(self.myCounter)
        sleep(1)

    def disabled(self) -> None:
        pass

    def publish(self) -> None:
        pass
