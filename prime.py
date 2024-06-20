n = int(input("Range: "))
for k in range(2, n + 1):
    s = 0
    for i in range(2, k):
        if k % i == 0:
            s = 1
            break
    if s == 0:
        print(k)

"""This is a program to count prime Numbers till a range is given by the user
1.n is a variable that will store the input given by the user
2.k will range from 2 to n{n+1 is given as for loop will count till n-1 not n}
3.i will range from 2 to k
4.s is a checker. It's initial value is 0.
5.if statement in the second loop checks if the number k is divided by i. i increases from 2 to k-1.
--Because prime numbers are divided by at least one number except 1 and themselves--
6.If k is indeed divided by a value of k then it will store s as 1 and break the loop
7.If not then s will stay 0 and at the end of the second loop and print the number which is a prime number
8.The first loop will continue till n=k(k<n+1)
"""
