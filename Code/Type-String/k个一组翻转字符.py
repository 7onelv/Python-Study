def reverse_k_group(str_in, k) -> str:
    """
    :param str_in: The first input list
    :param k: Reverse every k strings
    :return: The str_in after reverse
    """
    times = len(str_in) // k # 总共需要翻转几次
    remain = len(str_in) % k # 最后剩余的，不需要翻转的字符
    result = ''
    for i in range(1, times+1):
        for j in range(i*k-1, (i-1)*k-1, -1):
            result += str_in[j]
    if remain > 0: # 仅当有残余数的时候才执行以下
        result += str_in[-remain:] 
    return result
