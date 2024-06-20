f = open("Questions.txt", "w")
g = open("Answers.txt", "w")

num = int(input("How many Questions: "))
for i in range(1, num + 1):
    ques = input("Question: ")
    f.writelines(f"Question-1: {ques}\n")
    for i in range(1, 5):
        opt = input(f"Option-{i}: ")
        f.writelines(f"{i}. {opt} \n")
    ans = input("Answer: ")
    g.writelines(ans)

f.close()
g.close()
