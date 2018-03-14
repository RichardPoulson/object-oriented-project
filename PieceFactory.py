from CheckersPiece import *

class PieceFactory():

    pieceCollection = []
    def __init__(self):
        pass

    def getPiece(self, pieceOwner=None, pieceID=None, pieceLocation=None):
        newPiece = CheckersPiece(owner=pieceOwner, ID=pieceID, location=pieceLocation)
        return newPiece


'''
#Testing:
pieceF = PieceFactory()
p = pieceF.getPiece()
print(p.getOwner())
'''
