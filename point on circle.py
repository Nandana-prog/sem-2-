import math

x=int(input("enter x coordinate"))
y=int(input("enter x2"))
r=int (input("enter radius"))
x2=int(input("enter x2"))
y2=int(input("enter x2"))


s=math. pow((x2-x),2)
p=math. pow((y2-y),2)

distance=math.sqrt(s+p)
if distance==r:
    
    print("lies on circle")
elif distance>r:
    
    print("lies outside")

else:
    print("lies inside")
