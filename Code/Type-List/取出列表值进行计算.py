list_1 = eval(input())
a, b, c, d = list(map(int, list_1)) # 使用了map函数
print(f'{a / b * (c + d): .2f}') # 格式为f'{ :.2f}
