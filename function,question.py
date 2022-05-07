# def fun():
#     num=int(input("enter the number"))
#     if num%2==0:
#         print(num,"both are even number")
#     else:
#         print(num,"both are odd number")    
# fun()        

def fun(a,b):
    # num=int(input("enter the number"))
    i=0
    while i<len(a) and  i<len(b):
        if a[i]%2==0 and b[i]%2==0:
            print("both are even")
        else:
            print("not both even")
        i+=1
fun([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87] )        