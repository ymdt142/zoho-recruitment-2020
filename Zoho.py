n=int(input())
i=0
j=0
k=1
while(i<n):
    j=0
    while(j<n):
        a=i + j
        if(a==n-1):
            for ii in range(i+1):
                if(k<10):
                    print(k, end=" ")
                else:
                    print(k, end="")
                k+=1
                j+=1
        else:
            print(" ",end=" ")
        j+=1
    print("")
    i+=1
