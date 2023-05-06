# a-z
# 0-9
# ._time 1
# @ time 1
# . 2,3 
# sunny@gmail.com
import re
email_conditon="^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email:")
if re.search(email_conditon,user_email):
    print("Right Email❤️")
else:
    print("Wrong Email😒")