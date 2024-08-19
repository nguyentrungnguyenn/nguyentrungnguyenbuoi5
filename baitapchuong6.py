# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:20:47 2024

@author: Nguyen Trung Nguyen
Bài 1: Trung bình cộng a, b, c, d

a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
c=int(input("Nhập số nguyên c:"))
d=int(input("Nhập số nguyên d:"))
numbers = (a, b, c, d)
average = sum(numbers) / len(numbers)
print("Trung bình cộng của 4 số là:", average)

Bài 2: Tính tổng, hiệu, tích, thương, chia lấy dư, chia lấy nguyên

a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
Tong = a + b
print("Tổng của phép tính là:", Tong)
Hieu = a - b
print("Hiệu của phép tính là:", Hieu)
Tich = a * b
print("Tích của phép tính là:", Tich)
Thuong = a / b 
Thuong = round( a / b, 3)
print("Thương của phép tính là:", Thuong)
Chia_lay_du = a % b
print("Chia lấy dư của phép tính là:", Chia_lay_du)
Chia_lay_nguyen = a // b
print("Chia lấy nguyên của phép tính là:", Chia_lay_nguyen)

Bài 3: Tổng các chữ số của N

N = int(input("Nhập số nguyên dương N:"))
chu_so_hang_chuc = N // 10
chu_so_hang_don_vi = N % 10
Tong_cac_chu_so_cua_N = chu_so_hang_chuc + chu_so_hang_don_vi
if 10 <= N <= 99:
    print("Tổng các chữ số của N là:", Tong_cac_chu_so_cua_N)
else:
    print("Nhập lại số nguyên có hai chữ số!")

Bài 4: Giờ phút giây

ThoiGian = input("Nhập thời gian:")
Gio, Phut, Giay = map(int, ThoiGian.split(':'))
Tong_so_giay = Gio*3600 + Phut*60 + Giay
print("Tổng số giây là:", Tong_so_giay)

Bài 5: Tính số tuổi 

Nam_sinh = int(input("Nhập năm sinh:"))
Nam_hien_tai = 2024
Tuoi = Nam_hien_tai - Nam_sinh
print("Số tuổi của bạn là:", Tuoi)

Bài 6: Phương trình bậc 2

a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
c = float(input("Nhập số c:"))
print(f"Phương trình bậc 2: {a}X^2 + {b}X + {c} = 0")

Bài 7: MENU

print("============MENU============")
print("    1. Hu tieu")
print("    2. Chao long")        
print("    3. Banh canh")
print("    4. Bun rieu")
print("    5. Pho bo")
print("============================")
khach_chon = input("Moi nhap lua chon:")
print("============================")
print("Sự lựa chọn của bạn là: ", khach_chon)

Bài 8: Phép tính biểu thức A

A = ((32) ** 0.2) - ((1/64) ** -0.25) + ((8/27) ** (1/3))
print("Kết quả:", round(A, 3))

Bài 9: Tính giá trị biểu thức

import math
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
A = (math.sqrt(a) - math.sqrt(b)) / ((a ** (1/4)) - (b ** (1/4)))
B = (math.sqrt(a) + ((a * b) ** (1/4))) / ((a ** (1/4)) + (b ** (1/4)))
print("Kết quả của phép tính là:", A - B)
"""

