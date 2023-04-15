# using the randint (generating the number within a given range)
import random
# random_list=random.randint(1,30)
# print(random_list)



# print the random number
# number=random.random()
# print(number)

# using for loop to print the random number
# random_list=[]
# for i  in range(0,15):
#     number=random.randint(1,100)
#     random_list.append(number)
# print(random_list)

# Using random.sample()
random_list=random.sample(range(10,30),6)
print(random_list)
