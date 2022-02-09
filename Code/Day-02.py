from cmath import pi

# 摄氏度转换
f = float(input('输入需要转换的华氏温度'))
c = (f-32) / 1.8
print('%.2f 华氏温度转化后为 %.2f 摄氏温度' %(f,c))

# 圆的面积和周长计算
r = float(input('输入圆的半径'))
circum = 2 * r * pi
area = r ** 2 * pi
print('该圆的周长是 %.2f' %circum)
print('该圆的面积是 %.2f' %area) 

# 判断该年是不是闰年
year = int(input('请输入年份'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 # 闰年的判断标准为是4的倍数(但不是100的倍数）或是400的倍数。
print(is_leap)
