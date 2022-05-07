def fun():
    i=0
    while i<1000:
        j=1
        sum=0
        while j<i:
            if j%j==0:
                sum+=j
            j=j+1
        if sum==i:
          print(i,"perfect number")  
        else:
          print(i,"not perfect number")    
        i=i+1
fun()                  