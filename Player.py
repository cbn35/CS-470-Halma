import math
from Halma import Halma

class Player():
    def __init__(self, game, player):
        self.player = player
        self.turn = False
        self.moveTimer = game.tLimit

    def makeMove(self, game):
        #TODO
        return None

    def minimax():
        return

    def rankDistanceFromGoal(self, game, player):
        pawns = self.getPawnLocations(game, player)
        avgDistance = 0
        for pawn in pawns:
            avgDistance += self.avgDistanceFromGoal(game, player, pawn[0], pawn[1])
        return avgDistance/10

    def getPawnLocations(self, game, player):
        pawns = []
        for i in range(0, len(game.board)):
            for j in range(0, len(game.board)):
                if game.board[i][j] == player or game.board[i][j]-3 == player:
                    pawns.append((i,j))
        return pawns

    def avgDistanceFromGoal(self, game, player, x, y):
        winningLocations = self.getWinningLocations(game, player)
        avgDistance = 0
        for location in winningLocations:
            avgDistance += math.sqrt(pow(location[0]-x, 2) + pow(location[1]-y, 2))
        return avgDistance/len(game.board)

    def getWinningLocations(self, game, player):
        winningLocations = []
        if player == 2:
            for i in range(0, 4):
                for j in range(0, 4):
                    if game.board[i][j] == 4:
                        winningLocations.append((i,j))

        elif player == 1:
            for i in range(len(game.board) - 4, len(game.board)):
                for j in range(0, len(game.board)):
                    if game.board[i][j] == 5:
                        winningLocations.append((i,j))

        return winningLocations

class Node:
    def __init__(self, value=None):
        self.value = value
        self.minOrMax = None
        self.nextNode = None
        self.parent = None

    def getValue(self):
        return self.value

    def getNext():
        return self.nextNode

    def getParent():
        return self.parent

    def getMinMaxValue():


class miniMaxList:
    def __init__(self, root):
        self.root = Node()

    def addNode(self, newNode):
        if root.value == None:
            self.root = newNode
            newNode.minOrMax = "Max"
            newNode.next = None
        else:
            current = self.root
            while self.next != None:
                current.getNext()
            current.next = newNode

            if current.minOrMax == "Max":
                newNode.minOrMax = "Min"
            else:
                newNode.minOrMax = "Max"

            newNode.parent = current
            newNode.next = None
