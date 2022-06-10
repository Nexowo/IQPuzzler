from csv import list_dialects
from typing import List, Tuple

class Plateaux:
    def __init__(self, plateau : list) -> None:
        self.__plateaux = plateau

    def __str__(self) -> str:
        strself = ''
        for line in self.__plateaux:
            for elem in line:
                strself += str(elem)
            strself += '\n'
        return strself

    def get_plateau(self) -> list:
        new_plateaux = []
        for line in self.__plateaux:
            new_plateaux.append(line.copy())
        return new_plateaux

    def count_holes(self) -> List(int):
        plateau = self.get_plateau()
        pile = []
        result = []
        i, j = self.__first_zero_in(plateau)
        while i != -1:
            pile.append((i, j))
            count = 0
            while pile != []:
                i, j = pile.pop()
                if plateau[i][j] == 0:
                    count += 1
                    plateau[i][j] = 'X'
                    if i > 0:
                        pile.append((i - 1, j))
                    if i < len(plateau) - 1:
                        pile.append((i + 1, j))
                    if j > 0:
                        pile.append((i, j - 1))
                    if j < len(plateau[i]) - 1:
                        pile.append((i, j + 1))
            result.append(count)
            i, j = self.__first_zero_in(plateau)
        return result

    @staticmethod
    def __first_zero_in(plateau : list) -> Tuple(int, int):
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau[i][j] == 0:
                    return i, j
        return -1, -1