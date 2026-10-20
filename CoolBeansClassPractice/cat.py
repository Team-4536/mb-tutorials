class Cat:
    def __init__(
        self, pattern: str, sizeCategory: str, isAlive: bool, sizeteeth: float
    ) -> None:
        self.pattern = pattern
        self.sizeCategory: str = sizeCategory
        self.isAlive: bool = isAlive
        self.sizeteeth: float = sizeteeth

    def print(self) -> None:
        print("your cats has a " + self.pattern + "pattern ")
        print("your cat has a " + self.sizeCategory + "size")
        print("your cat is" + self.isAlive)
        print("your cat has")

    def getPattern(self):
        return self.pattern

    def getsizeCategory(self):
        return self.sizeCategory

    def getisAlive(self):
        return self.isAlive

    def getSizeTeeth(self):
        return self.sizeteeth


# print("your cat has a " + pattern + " pattern! \n  your cat is"
