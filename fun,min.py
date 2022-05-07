def fun():
    list=[8,6,4,8,4,50,2,7]
    i=0
    a=list[0]
    while i<len(list):
        if list[i]<a:
            a=list[i]
        i=i+1
    print(a)    
fun()            


