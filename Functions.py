
def multiplier():
    n=int(input('Limit-\n'))
    s=1
    for i in range(0,n):
        k=int(input())
        s=s*k
    print(s)
def adder():
    n=int(input('Limit-\n'))
    s=0
    for i in range(0,n):
        k=int(input())
        s=s+k
    print(s)
def squares():
    n=int(input('Limit-\n'))
    for i in range(1,n+1):
        s=i*i
        print(s)
def average(n):
   
    s=0
    for i in range(0,n):
        k=int(input('Number: '))
        s=s+k
    print('Average is', s/(i+1))  

# This is very very important. Be careful about i. i is the items in n which is a tupple.


def avg(*n):
    sum=0
    for i in n:
        sum= sum + i
    return sum/len(n)
