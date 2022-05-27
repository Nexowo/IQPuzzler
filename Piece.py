""" Class Piece that is defined by two attributes a 2 dimentional array, that represent a piece of the game, and transpose a boolean that inform if it's useful to transpose the piece.

@Author : jmaccou (Nexowo on GitHub)
"""

class Piece:
    def __init__(self, piece : list, transpose : bool) -> None:
        """ Constructor of the piece.
        :param piece: a 2 dimentional array, that can contain 2 values. A character to represent if the space is full and 0 if the space is empty.
        """
        self.__piece = piece
        self.__transpose = transpose

    def get_piece(self) -> list:
        return self.__piece

    def is_transposable(self) -> bool:
        return self.__transpose

    def rotation(self) -> None:
        self.__piece = [[self.__piece[j][i] for j in range(len(self.__piece))] for i in range(len(self.__piece[0])-1,-1,-1)]

    def transpose(self) -> None:
        assert self.__transpose
        self.__piece = [[self.__piece[row][col] for row in range(0,len(self.__piece))] for col in range(0,len(self.__piece[0]))]

    def __str__(self) -> str:
        strself = ''
        for line in self.__piece:
            for elem in line:
                strself += str(elem)
            strself += '\n'
        return strself