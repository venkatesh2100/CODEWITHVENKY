class Myclass:
    def __init__(self) -> None:
        self.__private = 0
        self._public = 0

    def setPublic(self, x: int):
        self._private = x
        print(self._private)

    def serPrivate(self, x: int):
        self.__pubilc = x
        print(self.__pubilc)


ans = Myclass()
ans.setPublic(10)
ans.setPublic(100)
