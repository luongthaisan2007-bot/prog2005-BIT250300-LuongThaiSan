# Bài 1
# Kiểm tra số chẵn

def is_even(n):
    return n % 2 == 0

num = int(input("Nhập số: "))
print(is_even(num))
# Bài 2
# Tìm số lớn nhất trong ba số

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

print("Số lớn nhất là:", max(a, b, c))
# Bài 3
# Hàm với đối số mặc định

def greet(name="Student"):
    print("Hello,", name + "!")

greet()
greet("An")
# Bài 4
# Kiểm tra tuổi hợp lệ

age = int(input("Nhập tuổi: "))

if 1 <= age <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")
  # Bài 5
# Đếm số lần xuất hiện của ký tự 'a'

text = input("Nhập chuỗi: ")

count = text.count('a')

print("Số lần xuất hiện của 'a':", count)
# Bài 6
# Chuyển độ C sang độ F

c = float(input("Nhập nhiệt độ C: "))

f = c * 9/5 + 32

print(f"{c}°C = {f:.2f}°F")
# Bài 7
# Tính BMI

weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

print(f"BMI = {bmi:.2f}")
# Bài 8
# Chia hai số và xử lý lỗi

try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))

    result = a / b

    print("Kết quả:", result)

except ZeroDivisionError:
    print("Không thể chia cho 0")

except ValueError:
    print("Dữ liệu nhập không hợp lệ")
  # Bài 9
# Tính căn bậc hai

import math

n = float(input("Nhập số: "))

if n < 0:
    print("Lỗi: Không tính được căn bậc hai của số âm")
else:
    print("Căn bậc hai là:", math.sqrt(n))
  # Bài 10
# Nhập thông tin 3 sinh viên

for i in range(1, 4):
    print(f"\nSinh viên {i}")

    name = input("Tên: ")

    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    avg = (toan + ly + hoa) / 3

    print("Tên sinh viên:", name)
    print(f"Điểm trung bình: {avg:.2f}")
