import math
from datetime import datetime

a = int(input("请输入三角形的第一条边："))
b = int(input("请输入三角形的第二条边："))
c = int(input("请输入三角形的第三条边："))
s = 1 / 2 * (a + b + c)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("此三角形面积为：", area)

# 输出当前计算机的系统日期和时间
now = datetime.now()
print(now)
now.strftime("%x")
now.strftime("%X")

# 字符串拼接
str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家名字：")
print("世界那么大，{}想去{}看看。".format(str1, str2))

# 整数序列求和
n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i + i
print("1到N求和结果：", sum)

# 九九乘法表输出
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:2} ".format(j, i, i * j), end='')
    print('')

# 1!+2!+3!+……+10!的结果
sum, tmp = 0, 1
for i in range(1, 11):
    tmp *= i
    sum += tmp
print("运算结果是：{}".format(sum))

# 猴子吃桃问题
n = 1
for i in range(5, 0, -1):
    n = (n + 1) << 1
print(n)

## 健康食谱输出
diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0, 5):
    for y in range(0, 5):
        if not (x == y):
            print("{} {}".format(diet[x], diet[y]))
