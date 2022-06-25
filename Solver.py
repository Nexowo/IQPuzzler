from email.errors import StartBoundaryNotFoundDefect
from typing import List
from Piece import Piece
from Plateaux import Plateaux

class Solver:
    def __init__(self, piece_collection : List[Piece], board : Plateaux):
        self.__list_piece = piece_collection.copy()
        self.__board = board

    def run(self) -> Plateaux :
        #TODO rewrite the function
        if self.__list_piece == []:
            return self.__board
        
        piece = self.__list_piece.pop()
        board = self.__board.get_plateau()
        for _ in range(piece.is_transposable()+1):
            for _ in range(4):
                for i in range(0,len(board)-len(piece.get_piece())+1):
                    for j in range(0,len(board[0])-len(piece.get_piece()[0])+1):
                        if self.__board.place_piece(piece, i, j):
                            if self.__minimum_piece_size() > self.__board.count_holes().sort().pop(0):
                                return self.run()
                            

    def __minimum_piece_size(self) -> int:
        min = -1
        for piece in self.__list_piece:
            if min == -1:
                min = piece.get_size()
            else:
                if min > piece.get_size():
                    min = piece.get_size()
        return min
