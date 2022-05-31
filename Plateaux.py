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

    def __iter__(self):
        return __PlateauxIterator(self)

class __PlateauxIterator:
    def __init__(self, plateau : Plateaux) -> None:
        self.__plateau = plateau
        self.__row = 0
        self.__col = 0

    def __next__(self) -> tuple:
        if self.__row == len(self.__plateau.get_plateaux()):
            raise StopIteration
        else:
            self.__col += 1
            if self.__col == len(self.__plateau.get_plateaux()[self.__row]):
                self.__col = 0
                self.__row += 1
            return (self.__row, self.__col)
