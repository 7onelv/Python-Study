s = str(input())
result = ''
for i in range(len(s)-1, -1, -1): # 反向遍历str中的元素，中间的值为-1
    result += s[i]
print(result)
