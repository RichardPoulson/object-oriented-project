from CheckersPiece import *

class PieceFactory():

    pieceCollection = []
    def __init__(self):
        pass

    def getPiece(self, pieceOwner=None):
        newPiece = CheckersPiece(owner=pieceOwner)
        return newPiece


'''
#Testing:
pieceF = PieceFactory()
p = pieceF.getPiece()
print(p.getOwner())
'''
