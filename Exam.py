f = open("Questions.txt", "r")
g = open("Answers.txt", "r")
a = 0
b = 0
c = g.read()

for i in f:
    print(i, end="")
    a += 1
    if a % 5 == 0:
        ans = str(input("Answer: "))

        if ans == c[b]:
            print("Correct")
        else:
            print("Incorrect")
        b += 1
f.close()
g.close()
