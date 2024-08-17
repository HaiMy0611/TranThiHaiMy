a= float(input("Nhập quãng đường(km ) : "))
if a<=1 :
   print ("tien taxi đi được là : 20k")
elif a<=3:
    print ("tiền taxi đi được là : ", a*13 ,"k")
elif 4<=a<=8:
    print ("tiền taxi đi được là : ", 3*13+(a-3)*12 ,"k")
elif a>8 and a<=100 :
    print ("tiền taxi đi đc là : ", 3*13+5*12+(a-8)*10, "k")
else : 
    print("tiền taxi đi được là : ", (3*13+5*12+(a-8)*10)-((3*13+5*12+(a-8)*10)*(8/100)), "k")
    