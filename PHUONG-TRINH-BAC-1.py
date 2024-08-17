a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a == 0:
    if b==0:
        print (" trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b/a
    print(f"Phương trình có nghiệm x={x}.")
