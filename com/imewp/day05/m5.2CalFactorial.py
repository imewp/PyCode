def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n


num = eval(input("请输入一个整数："))
print(fact(int(num)))
