# print this pattern
# 1
# 12
# 123
# 1234
# 12345


for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(j,end="");
    print()



# print this pattern
# 54321
# 4321
# 321
# 21
# 1

for i in range(1,6):
    k=6-i;
    for j in range(1,6):
        if(j<=6-i):
            print(k,end="")
            k-=1
        else:
            print("",end="")
            
    print()