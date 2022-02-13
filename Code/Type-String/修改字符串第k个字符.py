def change_str(txt, k, s):
    '''
    param txt: 输入文本
    param k: 替换位置
    s: 替换文本
    '''
    str1 = txt[0:k]
    str2 = txt[k+1:]
    return str1 + s + str2
