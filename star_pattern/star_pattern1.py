# print the pattern
# *
# **
# ***
# ****
# *****
# for i in range(1,6):                        
#     for  j in range(1,6):
#         if(j<=i):
#             print("*",end="")
#     print() 


# print the pattern
# *****
# ****
# ***
# **
# *

# for i in range (1,6):
#     for j in range(1,6):
#         if(j>=i):
#           print("*",end="")
#     print()


# print this pattern
#     *
#    **
#   ***
#  ****
# *****

for i in range(1,6):
    for j in range(1,6):
        if(j>=6-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    

# print this pattern
# *****
#  ****
#   ***
#    **
#     *

# for i in range(1,5):
#     for j in range(1,5):
#         if(j>=6-i):
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()