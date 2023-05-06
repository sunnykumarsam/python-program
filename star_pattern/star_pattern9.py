# *
# **
# ***
# ****
# ***
# **
# *


# row=int(input("Enter the number of rows:-"))
# for i in range(row):
#     print("*"*(i+1))
# for j in range(row):
#     print("*"*(row-j-1))


# print this pattern
  
#     *
#  *  *
# * * *
#   * *
#     *


# for i in range(1,row):
#     for j in range(1,row):
#         if(j>=row-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
# for i in range(1,row):
#     if(i==3):
#         break
#     for j in range(1,row):
#         if(j>i):
#          print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


row=int(input("Enter the number of row:-"))
for i in range(1,row):
    for j in range(1,row):
        if(j>=row-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
for i in range(1,row):
    if(i==row-1):
        break
    for j in range(1,row):
        if(j>i):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    