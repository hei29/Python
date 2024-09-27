
# 数值类型
# int整型  任意大小的整数
num = 4
# 获取类型
print(type(num)) #<class 'int'>

# float浮点型 小数
mum2 = 1.2
# <class 'float'>
print(type(mum2))

# bool布尔型 True False
# 严格区分大小写True False
# print(type(true)) 报错
# true = True
# print(true) # True
# 布尔值可以当做整型对待 True 1 False 0
# print(True + False) 1 + 0 = 1

# complex 复数型
# 固定写法: z = a + bj  --a是实部，b是虚部，j是虚数单位(虚数单位只能用j)
mi = 1 + 2j
mu = 3 + 4j
# (4+6j) <class 'complex'>
print(mi + mu, type(mi + mu))