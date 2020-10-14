import math

a = int(input("请输入三角形的第一条边："))
b = int(input("请输入三角形的第二条边："))
c = int(input("请输入三角形的第三条边："))
s = 1 / 2 * (a + b + c)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("此三角形面积为：", area)
