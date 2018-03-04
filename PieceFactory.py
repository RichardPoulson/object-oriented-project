from CheckersPiece import *

class PieceFactory():

    pieceCollection = []
    def __init__(self):
        pass

    def getPiece(self):
        newPiece = CheckersPiece(owner='X')
        return newPiece


'''
#Testing:
pieceF = PieceFactory()
p = pieceF.getPiece()
print(p.getOwner())
'''
