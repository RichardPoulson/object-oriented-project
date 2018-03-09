from CheckersPiece import *

class PieceFactory():

    pieceCollection = []
    def __init__(self):
        pass

    def getPiece(self, pieceOwner=None, pieceLocation=None):
        newPiece = CheckersPiece(owner=pieceOwner, location=pieceLocation)
        return newPiece


'''
#Testing:
pieceF = PieceFactory()
p = pieceF.getPiece()
print(p.getOwner())
'''
