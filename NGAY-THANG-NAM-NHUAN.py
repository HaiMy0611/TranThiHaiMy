a = float(input("Nhập ngày : "))
b = float(input("Nhập tháng : "))
c = float(input("Nhập năm : "))
if (c%4==0 and c%100!=0) or c%400==0:
   nam_nhuan = True 
else:
   nam_nhuan = False 
if b==2:
    if nam_nhuan :
       so_ngay_trong_thang= 29 
    else : 
        so_ngay_trong_thang= 28 
elif b in[4,6,9,11]:
    so_ngay_trong_thang= 30 
else :
   so_ngay_trong_thang= 31 
if 1<=b<=12:
    if 1<=a<=so_ngay_trong_thang:
        if nam_nhuan:
            print(f"năm {c} là năm nhuận ")
        else:
            print (f"năm {c} không là năm nhuận ")
    else:
        print(f"{a}/{b}/{c} ngày không hợp lệ ")
else :
    print(f"{a}{b}{c} tháng không hợp lệ ")
    

    
