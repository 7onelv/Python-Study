# 用户身份验证
username = input('请输入用户名')
password = input('请输入密码')
# 设定用户为admin/asd123
if username == "admin" and password == "asd123": 
    print('验证成功')
else:
    print('验证失败')

# 分段函数求值
x = float(input('请输入一个数字'))
if x > 1:
    result = x * 3 - 5
elif x >= -1:
    result = x + 2
else:
    result = x * 5 + 3
print('f(%.2f) = %.2f' %(x, result))

# 英制单位英寸和公制单位厘米互换
value = float(input('请输入长度:'))
unit = input('请输入单位')
if unit == 'inch' or unit == '英寸': # 注意这块or连接的是完整的逻辑确认
    print('转换后为 %.2f 厘米' %(value * 2.54)) # 这块%之后必须加()才能够使用
elif unit == 'cn' or unit == '厘米':
    print('转换后为 %.2f 英寸' %(value / 2.54))
else: 
    print('请输入有效的单位')

# 百分制成绩转换为等级制成绩
score = float(input('请输入成绩'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else: # 最后一个逻辑关键字必须使用else
    grade = 'Failed'
print('该成绩的等级是', grade)

# 输入三条边长，如果可以构成三角形就计算周长和面积
a = float(input('请输入边长1'))
b = float(input('请输入边长2'))
c = float(input('请输入边长3'))
if a + b > c and a + c > b and b + c > a: # 这块不用加括号因为加减乘除的运算顺序大于比较符号
    print('该三角形的周长为 %.2f' %(a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('该三角形的面积为 %.2f' %area)
else:
    print('提供的三条边长不能组成三角形')
