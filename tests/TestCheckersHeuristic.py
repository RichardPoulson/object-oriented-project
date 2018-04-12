import unittest
from CheckersHeuristic import *
from CheckersBoard import *
from HumanPlayer import *

class TestCheckersHeuristicMethods(unittest.TestCase):
    def setUp(self):
        self.firstCheckersBoard = CheckersBoard()
        self.secondCheckersBoard = CheckersBoard()
        self.firstPlayer = HumanPlayer('TestPlayer')
        self.secondPlayer = HumanPlayer('SecondTestPlayer')
        self.checkersHeuristic =\
            CheckersHeuristic(self.firstCheckersBoard, self.firstPlayer)

    # does the getter for CheckersHeuristic.computerPlayer work?
    def test_get_computer_player(self):
        currentComputerPlayer = self.checkersHeuristic.getComputerPlayer()
        self.assertEqual(currentComputerPlayer, self.firstPlayer)

    # does the getter for CheckersHeuristic.checkersBoard work?
    def test_get_checkers_board(self):
        currentCheckerBoard = self.checkersHeuristic.getCheckersBoard()
        self.assertEqual(currentCheckerBoard, self.firstCheckersBoard)

    # does the setter for CheckersHeuristic.computerPlayer work?
    def test_set_computer_player(self):
        self.checkersHeuristic.setComputerPlayer(self.secondPlayer)
        currentComputerPlayer = self.checkersHeuristic.getComputerPlayer()
        self.assertEqual(currentComputerPlayer, self.secondPlayer)

    # does the setter for CheckersHeuristic.checkersBoard work?
    def test_set_checkers_board(self):
        self.checkersHeuristic.setCheckersBoard(self.secondCheckersBoard)
        currentCheckerBoard = self.checkersHeuristic.getCheckersBoard()
        self.assertEqual(currentCheckerBoard, self.secondCheckersBoard)

    # not sure how to test the getUtilityMethod at this point.

if __name__ == '__main__':
    unittest.main()