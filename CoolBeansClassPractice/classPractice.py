class ClassName:
    def __init__(self, thing: str) -> None:
        print(thing)
        self.thing = thing
    def isCoolBeans(self, text:str) -> bool:
        if self.thing in text:
            return True
        else:
            return False




A: ClassName = ClassName("a")
if A.isCoolBeans("cool"):
    print("there is cool beans in you text")
else:
    print("no soy cool beans")