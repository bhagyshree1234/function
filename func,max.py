def fun():
    a=[3,5,7,34,2,89,2,5]
    i=0
    b=a[0]
    while i<len(a):
        if a[i]>b:
            b=a[i]
        i=i+1
    print(b)
fun()            