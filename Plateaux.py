class Plateaux:
    def __init__(self, plateau : list) -> None:
        self.__plateaux = plateau

    def get_plateaux(self) -> list:
        return self.__plateaux

    def __str__(self) -> str:
        strself = ''
        for line in self.__plateaux:
            for elem in line:
                strself += str(elem)
            strself += '\n'
        return strself
