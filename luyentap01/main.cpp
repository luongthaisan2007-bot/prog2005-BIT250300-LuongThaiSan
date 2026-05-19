# Bài 1
# Tạo các biến với các kiểu dữ liệu khác nhau

so_nguyen = 10
so_thuc = 3.14
chuoi = "Hello Python"

print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)
  
# Bài 2
# Tính chu vi hình tròn

PI = 3.14
r = 5

chu_vi = 2 * PI * r

print("Chu vi hình tròn là:", chu_vi)
  
 # BÀI 3: Thực hiện các phép toán cơ bản với hai số
# ============================================================
print("\n=== BÀI 3 ===")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không xác định (chia cho 0)"

print(f"Tổng:    {a} + {b} = {tong}")
print(f"Hiệu:    {a} - {b} = {hieu}")
print(f"Tích:    {a} × {b} = {tich}")
print(f"Thương:  {a} ÷ {b} = {thuong}") 
  
  # Bài 4
# Hàm tính tổng hai số

def sum_two_numbers(a, b):
    return a + b

ket_qua = sum_two_numbers(5, 7)

print("Tổng của hai số là:", ket_qua)
  
  # Bài 5
# Khai báo, xử lý và hiển thị thông tin cá nhân

name = "San"
age = 18
average_score = 8.5

# Hiển thị kiểu dữ liệu
print(type(name))
print(type(age))
print(type(average_score))

# Tạo biến mới
age_next_year = age + 1
doubled_score = average_score * 2

# In thông tin
print("Tên:", name)
print("Tuổi hiện tại:", age)
print("Tuổi năm sau:", age_next_year)
print("Điểm trung bình:", average_score)
print("Điểm sau khi nhân đôi:", doubled_score)
