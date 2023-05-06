# print triangle
# for i in range(6):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# print hollow triangle
for i in range(6):
    for j in range(6):
        if(j==i or i==5 or j==0 ):
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()
