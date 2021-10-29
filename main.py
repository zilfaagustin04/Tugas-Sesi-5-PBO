class AC:
    _suhu = []
    __tingkatsuhu = None

    def __init__(self):
        self.__scan()

    def __scan(self):
        print('scan suhu')
        self._suhu = [16, 18, 20]

    def _setSuhu(self):
        print('set tingat suhu')
        self.__tingkatsuhu = self._suhu[0]

    def getTingkatSuhu(self):
        return self.__tingkatsuhu


# Car
class tingkatsuhu(AC):
    def __init__(self):
        super(tingkatsuhu, self).__init__()
        self._setSuhu()



carAC = tingkatsuhu()
print(carAC.getTingkatSuhu())