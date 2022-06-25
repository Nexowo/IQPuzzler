from typing import List, Tuple
from Piece import Piece

""" This class is used to represent the gameboard of IQPuzzler.
It is composed of a double dimention list where 0 is a empty space, X is a non disponible space and any other caracter is a piece.
@Author: Jean Maccou
"""

class Plateaux:
    def __init__(self, plateau : list) -> None:
        """ Constructor of the plateau, we copy the new plateau in the private attribute __plateaux."""
        self.__plateaux = []
        for line in plateau:
            self.__plateaux.append(line.copy())

    def __str__(self) -> str:
        strself = ''
        for line in self.__plateaux:
            for elem in line:
                strself += str(elem)
            strself += '\n'
        return strself

    def get_plateau(self) -> list:
        """:return: a double dimentional list that is a copy of the plateau"""
        new_plateaux = []
        for line in self.__plateaux:
            new_plateaux.append(line.copy())
        return new_plateaux

    def count_holes(self) -> List[int]:
        """:return: a list of int, where the size of the list is the number of holes in the plateau and the values is the size of the different holes."""
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

    def place_piece(self, piece : Piece, x : int, y : int) -> bool:
        """ Test if a piece can be placed on a board, and place it.
        :param piece: the piece to place on the board.
        :param x: the x coordiante to place the top left corner of the piece.
        :param y: the y coordiante to place the top left corner of the piece.
        :return: True if the piece can be placed, false otherwise
        """
        new_plat = self.get_plateau()
        piece_copy = piece.get_piece()
        for i in range(len(piece_copy)):
            for j in range(len(piece_copy[i])):
                if new_plat[i + x][j + y] != 0 and piece_copy[i][j] != 0:
                    return False
                if piece_copy[i][j] != 0:
                    new_plat[i + x][j + y] = piece_copy[i][j]
        self.__plateaux = new_plat
        return True

    @staticmethod
    def __first_zero_in(plateau : list) -> Tuple[int, int]:
        """Static method that find the first zero in the board and return the coordinates of this one.
        :param plateau: the board to search in.
        ;return: a tuple of cordinates of the first zero in the board, or (-1, -1) if there is no zero in the board."""
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau[i][j] == 0:
                    return i, j
        return -1, -1