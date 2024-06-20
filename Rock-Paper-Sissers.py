# Procedural
# import random

# ms = 0
# cs = 0
# q = int(input("How many rounds do you want to play?\n"))
# print("1. Rock 2. Paper 3. Sisser 4. exit")

# for i in range(0, q):
#     print(f"Round-{i+1}:")
#     c = random.randint(1, 3)
#     i = int(input())
#     if i == 1:
#         print("You played Rock")
#     if i == 2:
#         print("You played Paper")
#     if i == 3:
#         print("You played Sisser")
#     if c == 1:
#         print("Computer played Rock")
#     if c == 2:
#         print("Computer played Paper")
#     if c == 3:
#         print("Computer played Sisser")
#     if i == 1 and c == 2:
#         cs += 1
#         print("Computer won")
#     elif i == 1 and c == 3:
#         ms += 1
#         print("You won")
#     elif i == 2 and c == 3:
#         print("Computer won")
#         cs += 1
#     elif i == 2 and c == 1:
#         print("You won")
#         cs += 1
#     elif i == 3 and c == 1:
#         print("Computer won")
#         cs += 1
#     elif i == 3 and c == 2:
#         ms += 1
#         print("You won")
#     elif i == c:
#         print("Draw")
#     else:
#         print("You gave Wrong Input!")
#     print(f"You: {ms} & Computer: {cs}")
 #OOP
    
from random import randint


class game:
    def playername(self):
        self.name = str(input("Name of the player: "))
        self.player_score=int()
        self.computer_score=int()
    def start(self):
        self.player_number = input("1. Stone 2. Paper 3. Scissors\n")
        self.computer_number = randint(1, 3)     
    def hand(self, value):
        self.val = int(value)
        if self.val == 1:
            return "Stone"
        if self.val == 2:
            return "Paper"
        if self.val == 3:
            return "Scissors"
        else:
            return "Invalid Input"
    def game(self):
        self.player_number = int(self.player_number)
        self.winner = str()
        if self.player_number == self.computer_number:
            self.winner = "Draw"
        elif self.computer_number == 1 and self.player_number == 2:
            self.player_score+=1
            self.winner = f"{self.name} has won"
        elif self.computer_number == 1 and self.player_number == 3:
            self.computer_score+=1
            self.winner = "Computer has won"
        elif self.computer_number == 2 and self.player_number == 1:
            self.computer_score+=1
            self.winner = "Computer has won"
        elif self.computer_number == 2 and self.player_number == 3:
            self.player_score+=1
            self.winner = f"{self.name} has won"
        elif self.computer_number == 3 and self.player_number == 1:
            self.player_score+=1
            self.winner = f"{self.name} has won"
        elif self.computer_number == 3 and self.player_number == 2:
            self.computer_score+=1
            self.winner = "Computer has won"
        else:
            self.winner = "Invalid Input"


a = game()
n = int(input("How many times do you want to play?\n"))
a.playername()
for i in range(0, n):
    a.start()
    print(f"{a.name} played {a.hand(a.player_number)}")
    print(f"Computer played {a.hand(a.computer_number)}")
    a.game()
    print(f"{a.winner}!")
print(a.computer_score,a.player_score)