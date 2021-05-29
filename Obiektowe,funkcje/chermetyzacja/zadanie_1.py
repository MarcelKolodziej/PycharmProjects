class Zwierzak:
    def __init__(self,wiek):
        self.wiek = wiek
    @property
    def wiek(self):
        return self.__wiek
    @wiek.setter
    def wiek(self,wiek):
        if wiek < 0:
            self.__wiek = 0
        elif wiek > 200:
            self.__wiek = 200
        else:
            self.__wiek = wiek

slon = Zwierzak(205)
print(slon.wiek)
slon.wiek = 40
print(slon.wiek)
slon.wiek = -55
print(slon.wiek)