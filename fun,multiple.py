def fun():
    a=[5, 10, 50, 20]
    b=[2, 20, 3, 5]
    i=0
    mul=[]
    while i<len(a):
        h=a[i]*b[i]
        mul.append(h)
        i=i+1
    print(mul)
fun()    


list=[1,4,5,2,3,7,8,9]
i=0
a=0
while i<len(list):
    if list[i]>a:
        a=list[i]
    i=i+1
print(a)
i=0
b=list[0]
while i<len(list):
    if list[i]!=a and list[i]>b:
        b=list[i]
    i=i+1
print(a+b)                





 