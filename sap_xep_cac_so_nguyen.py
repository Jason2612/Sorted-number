"""
Viết chương trình cho người dùng nhập vào 3 số nguyên bất kỳ,
sau đó sẽ in ra thứ tự tăng dần của 3 số nguyên được nhập vào.
"""
def sort_number(num1, num2, num3):
    temp = 0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return (num1, num2, num3)

x = int(input("Nhap so dau tien: "))
y = int(input("Nhap so thu hai: "))
z = int(input("Nhap so thu ba: "))

a, b, c = sort_number(x, y, z)
print("Cac so ban dau: ", x, y, z)
print("Cac so sau khi sap xep: ", a, b, c)
