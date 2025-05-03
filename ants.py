import abc

class Ant:
    i, j = 0, 0
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def LeftTurn(self):
        """LeftTurn"""
    @abc.abstractmethod
    def RightTurn(self):
        """RightTurn"""
    @abc.abstractmethod
    def Step(self):
        """Step"""
    @abc.abstractmethod
    def FixCoords(self):
        """FixCoords"""


class HexAnt(Ant):
    direction = "RR"
    rule = "54544"
    
    def RightTurn(self):
        if self.direction == "RR":
            self.direction = "RD"
        elif self.direction == "RD":
            self.direction = "LD"
        elif self.direction == "LD":
            self.direction = "LL"
        elif self.direction == "LL":
            self.direction = "LU"
        elif self.direction == "LU":
            self.direction = "RU"
        elif self.direction == "RU":
            self.direction = "RR"

    def LeftTurn(self):
        if self.direction == "RR":
            self.direction = "RU"
        elif self.direction == "RU":
            self.direction = "LU"
        elif self.direction == "LU":
            self.direction = "LL"
        elif self.direction == "LL":
            self.direction = "LD"
        elif self.direction == "LD":
            self.direction = "RD"
        elif self.direction == "RD":
            self.direction = "RR"

    def Step(self):
        if self.direction == "RR":
            self.j += 1
            return
        if self.direction == "LL":
            self.j -= 1
            return
        if self.i % 2 == 1 and self.direction[0] == 'R':
            self.j += 1
        elif self.i % 2 == 0 and self.direction[0] == 'L':
            self.j -= 1
        if self.direction[1] == 'U':
            self.i -= 1
        elif self.direction[1] == 'D':
            self.i += 1

    def FixCoords(self, N, M):
        if self.i >= N:
            self.i = 0
        if self.j >= M:
            self.j = 0
        if self.i < 0:
            self.i = N - 1
        if self.j < 0:
            self.j = M - 1

    def MakeHexMove(self, field, gl):
        old_colour = field[self.i][self.j].colour
        new_colour = (old_colour + 1) % len(self.rule)
        for i in range(int(self.rule[old_colour])):
            self.LeftTurn()
        field[self.i][self.j].colour = new_colour
        field[self.i][self.j].Draw(gl)
        self.Step()

class SquareAnt(Ant):
    direction = [0, 1]
    rule = "LR"
    def LeftTurn(self):
        if self.direction == [0, 1]:
            self.direction = [-1, 0]
        elif self.direction == [-1, 0]:
            self.direction = [0, -1]
        elif self.direction == [0, -1]:
            self.direction = [1, 0]
        else:
            self.direction = [0, 1]

    def RightTurn(self):
        self.LeftTurn()
        self.LeftTurn()
        self.LeftTurn()

    def Step(self):
        self.i += self.direction[0]
        self.j += self.direction[1]

    def FixCoords(self, N, M):
        if self.i >= N:
            self.i = 0
        if self.j >= M:
            self.j = 0
        if self.i < 0:
            self.i = N - 1
        if self.j < 0:
            self.j = M - 1

    def MakeMove(self, field, gl):
        old_colour = field[self.i][self.j].colour
        new_colour = (old_colour + 1) % len(self.rule)
        if self.rule[old_colour] == 'R':
            self.RightTurn()
        elif self.rule[old_colour] == 'L':
            self.LeftTurn()
        elif self.rule[old_colour] == 'U':
            self.LeftTurn()
            self.LeftTurn()
        elif self.rule[old_colour] == 'S':
            self.LeftTurn()
            self.RightTurn()

        field[self.i][self.j].colour = new_colour
        field[self.i][self.j].Draw(gl)
        self.Step()