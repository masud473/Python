from random import randint


class Game:

    def __init__(self) -> None:
        self.name = str(input("Player Name: "))
        self.moves = set()


class Graph:
    a = b = c = d = e = f = g = h = i = " "

    def graphing(self, move, word):
        self.word = word
        self.move = int(move)
        if self.move == 7 and self.a == " ":
            self.a = self.word
        elif self.move == 8 and self.b == " ":
            self.b = self.word
        elif self.move == 9 and self.c == " ":
            self.c = self.word
        elif self.move == 4 and self.d == " ":
            self.d = self.word
        elif self.move == 5 and self.e == " ":
            self.e = self.word
        elif self.move == 6 and self.f == " ":
            self.f = self.word
        elif self.move == 1 and self.g == " ":
            self.g = self.word
        elif self.move == 2 and self.h == " ":
            self.h = self.word
        elif self.move == 3 and self.i == " ":
            self.i = self.word

    def show(self):
        print("___________________  ___________________")
        print("|     |     |     |  |     |     |     |")
        print(f"|  {self.a}  |  {self.b}  |  {self.c}  |  |  7  |  8  |  9  |")
        print("|_____|_____|_____|  |_____|_____|_____|")
        print("___________________  ___________________")
        print("|     |     |     |  |     |     |     |")
        print(f"|  {self.d}  |  {self.e}  |  {self.f}  |  |  4  |  5  |  6  |")
        print("|_____|_____|_____|  |_____|_____|_____|")
        print("___________________  ___________________")
        print("|     |     |     |  |     |     |     |")
        print(f"|  {self.g}  |  {self.h}  |  {self.i}  |  |  1  |  2  |  3  |")
        print("|_____|_____|_____|  |_____|_____|_____|")


class checker:

    def __init__(self, set) -> None:
        self.set = set
        self.end = 0

    def check(self):
        if {1, 2, 3}.issubset(self.set):
            self.end = 1
        elif {4, 5, 6}.issubset(self.set):
            self.end = 1
        elif {7, 8, 9}.issubset(self.set):
            self.end = 1
        elif {1, 4, 7}.issubset(self.set):
            self.end = 1
        elif {2, 5, 8}.issubset(self.set):
            self.end = 1
        elif {3, 6, 9}.issubset(self.set):
            self.end = 1
        elif {1, 5, 9}.issubset(self.set):
            self.end = 1
        elif {3, 5, 7}.issubset(self.set):
            self.end = 1


Player1 = Game()
Player2 = Game()
graph = Graph()
graph.show()
# auto = int(input("Who do you want to play against?\n1) Human\n2) Computer\n"))
auto = 1
while True:

    Player1_move = int(input(f"{Player1.name} give your Move: "))
    while Player1_move in Player1.moves or Player1_move in Player2.moves:
        Player1_move = int(
            input(
                f"Sorry {Player1.name}! This input has already been given. Please give another Input\n"
            )
        )
    if Player1_move < 1 or Player1_move > 9:
        Player1_move = int(
            input(
                f"Sorry {Player1.name}! This input has already been given. Please give another Input\n"
            )
        )
    else:
        Player1.moves.add(Player1_move)
        graph.graphing(Player1_move, "X")
        graph.show()
        check_1 = checker(Player1.moves)
        check_1.check()
    if check_1.end == 1:
        print(f"{Player1.name} has won!")
        break
    if {1, 2, 3, 4, 5, 6, 7, 8, 9} == Player1.moves.union(Player2.moves):
        print("Tie")
        break
    if auto == 1:
        Player2_move = int(input(f"{Player2.name} give your Move: "))
    if auto == 2:
        Player2_move = randint(1, 9)
    while Player2_move in Player1.moves or Player2_move in Player2.moves:
        if auto == 1:
            Player2_move = int(
                input(
                    f"Sorry {Player2.name}! This input has already been given. Please give another Input\n"
                )
            )
        if auto == 2:
            Player2_move = randint(1, 9)
    if Player2_move < 1 or Player2_move > 9:
        if auto == 1:
            Player2_move = int(
                input(
                    f"Sorry {Player2.name}! This input has already been given. Please give another Input\n"
                )
            )

    else:
        Player2.moves.add(Player2_move)
        graph.graphing(Player2_move, "O")
        graph.show()
        check_2 = checker(Player2.moves)
        check_2.check()
    if check_2.end == 1:
        print(f"{Player2.name} has won!")
        break
