s=str(input("Input: "))
rev=str()
j=len(s)-1
for i in range(0,len(s)):
    rev+=s[j]
    j-=1

print(int(rev))