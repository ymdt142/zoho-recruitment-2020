n=5
i=0
j=0
k=1
while(i<n):
    j=0
    while(j<n):
        if(i+j==n-1):
            for ii in range(i+1):
                print(str(k),end="")
                k+=1
        else:
            print(" ",end="")
        j+=1
    print("")
    i+=1
