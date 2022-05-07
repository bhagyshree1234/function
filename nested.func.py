# list=[[1,2[3,4],3,[4,5],5]]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         # if j%2==0:
#         a.append(list[i][j])
#         j=j+1
#     i=i+1
# print(a)
# # list2=str(a)
# i=0
# b=[]  
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

a=[[1,2,[3,4],3,[4,5],5]]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
i=0
c=[]
while i<len(b):
    if type(b[i])==list:
        j=0
        while j<len(b[i]):
            c.append(b[i][j])
            j+=1
    else:
        c.append(b[i])
    i+=1
print("list:",c)
i=0
max=0
while i<len(c):
    if max<c[i]:
        max=c[i]
    i+=1
print("maximun numb:",max)
i=0
min=0
while i<len(c):
    if min>c[i]:
        min=c[i]
    i+=1
print("minimum numb:",min)
i=0
d=[]
e=[]
while i<len(c):
    if c[i]%2==0:
        d.append(c[i])
    else:
        e.append(c[i])
    i+=1
print(d,e)







