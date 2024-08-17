import math

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x=-c/b
        print("phương trình có nghiệm x= {x}", x)
else:
        delta = b**2 - 4*a*c
if delta > 0:
   x1 = -b + math.sqrt(delta)/(2*a)
   x2 = -b - math.sqrt(delta)/(2*a)
   print("Phương trình có hai nghiệm phân biệt :")
   print("x1:", x1 )
   print("x2:", x2 )
elif delta ==0:
       x=-b/2*a 
       print("phương trình có nghiệm kép x=", x)
else :
   print("phương trình vô nghiệm  ")
