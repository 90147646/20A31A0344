n=int(input("Enter the upper value:"))
for i in range(1,n):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
            else:
                print(i)
