n = float(input("Nhập điểm trung bình GPA: "))
if n < 3.5:
    print("Học lực Kém.")
elif 3.5 <= n <=5.0:
    print("Học lực yếu.")
elif 5.0 <= n <= 7.0:
    print("Học lực Trung bình.")
elif 7.0 <= n <= 8.0:
    print("Học lực Khá.")
elif 8.0 <= n <= 9.0:
    print("Học lực Giỏi.")
elif 9.0 <= n <= 10:
    print("Học lực Xuất sắc.")
else:
    print("Điểm không phù hợp.")