import cmath
a=int(input("Enter the number(a!=0)"))
b=int (input("Enter the second number:-"))
c=int(input("Enter the third number:-"))
## formula  for discriminant

d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)

print("The root are ",root1,"and",root2)