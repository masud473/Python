# lists----

a=[i for i in range(1,51) if i%2==0]
b=[i for i in range(51,101) if i%2!=0]
c=[1,1,5,6,74,26,45,15,48,3,6,8,68,4,8,1,68,4,65,41,85,65,48,1,21,3,51]
d=[98,45,89,15,48,35,102]
z=a+b+c+d

z.sort()
print('Sorted list:\n', z)
# x=[]
# y=[]
# for k in range(0,len(z)-1):
#     if(z[k]!=z[k+1]):
#         x.append(z[k])
# if(z[len(z)-1]==z[len(z)-2]):
#     x.append(z[len(z)-1])
# else:
#     x.append(z[len(z)-1])
# print('Items listed once:\n',x)
# for k in range(z[0],z[len(z)-1]+1):
#     s=0
#     for i in z:
#         if(k==i):
#             s=1
        
#     if(s==0):
#         y.append(k)
# print('List of items not in the list\n',y)
# x1=[]
# x0=[]
# xn=[]
# for k in range(z[0],z[len(z)-1]+1):
#     if(z.count(k)==1):
#         x1.append(k)
#     if(z.count(k)==0):
#         x0.append(k)
#     if(z.count(k)>1):
#         xn.append(k)
# print('Repeated:\n',xn)
# print('Once\n',x1)
# print(xn)

'''The best method to create no repeat list is to
create a set or convert a list to set ''' 
        
l=set(z) 
print(l)