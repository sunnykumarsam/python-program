# print the square 

# for i in range(8):
#     for j in range(8):
#         print("*",end=" ")
#     print()


# *          *
# *          *
# *          *
# *          *
# *          *
# n=8
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# print + pattern
n=5
# for i in range(n):
    # for j in range(n):
        # if(j==2 or i==2):
        # if(i==n//2 or j==n//2):    # this is another logic to print the plus
            # print("&",end=" ")
        # else:
            # print(" ",end=" ")
    # print()


            # *        *
            #  *     *
            #     *
            #  *     *
            #*         *
for i in range(1,6):
    for j in range(1,6):
        if(j==i or j==6-i):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
