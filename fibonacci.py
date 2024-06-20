
n=int(input('Range: '))
a=0
b=1
print(0)
print(1)
for i in range(0,n-2):
   c=a+b
   print(c)
   a=b
   b=c 
'''This is a program for fibonacci sequence
1.n is an input given by user which is the range or number of items in the sequence and count starts from 0.
2.a=0 and b=1 it is related to the main calculation. 0 and 1 will be printed as it is.
3.i is a counter which will count till the n of items are shown. range is 0 to n-3(<n-2). 2 counts are decreased for 0 and 1 are already printed.
4. c=a+b and it is the next item in the sequense and the only item that will be printed as a part of the loop
5. The next stage is switch. as a will now take the value of b and b will take the value of c to create the next c or item.
6. Loop will continue till a n-2 is reached

'''