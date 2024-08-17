a = float (input("Chiều dài cạnh thứ nhất: "))
b = float (input("Chiều dài cạnh thứ hai: "))
c = float (input("Chiều dài cạnh thứ ba: "))

#a,b,c có phải là 3 cạnh của tam giác và đó là tam giác gì?
if a+b>c or a+c>b or b+c>a:
    print ("a,b,c là 3 cạnh của tam giác.")
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print ("Đó là tam giác vuông.")
    elif a==b or a==c or b==c:
        print ("Đó là tam giác cân.")
    elif a==b==c:
        print ("Đó là tam giác đều.")
    else:
        print ("Đó là tam giác thường.")
else:
    print ("a,b,c không là 3 cạnh của tam giác.")




