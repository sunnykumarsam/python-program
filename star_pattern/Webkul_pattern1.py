
# for i in range(1,5):
#     for j in range (1,5):
#         if(i>=j):
#             print('*',end=" ")
#     print()
# for i in range(1,9):
#     print('*',end=" ")
# if(i==9/2-1) or (i==9/2+1):
#     print(" *")
# elif(i==9/2):
#     print("***")
# for i in range(1,5):
#     for j in range(1,5):
#         if(i<=j):
#             print("*",end=" ")
#     print()
n=8
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<n/2 and j<=i) or (i>n/2 and j<n-i) or (i==n/2):
            print("*")
        else:
            print(" ")

    if(i==n/2-1) or (i==n/2+1):
        print(" *")        
    elif (i==n/2):
        print("***")
