class AC:
    __suhu = []
    __tingkatsuhu = None

    def _init_(self):
        self.__scan()

    def __scan(self):
        print('scan suhu')
        self.__suhu = [16, 18, 20]

    def _setSuhu(self):
        print('set tingat suhu')
        self._tingkatsuhu = self._suhu[18]

    def getTingkatSuhu(self):
        return self.__tingkatsuhu


# Car
class tingkatsuhu(AC):
    def _init_(self):
        super(tingkatsuhu, self)._init_()
        self._setSuhu()



carAC = tingkatsuhu()
print(carAC.getTingkatSuhu())