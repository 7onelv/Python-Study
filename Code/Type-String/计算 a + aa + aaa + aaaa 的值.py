def calculate_sum(int_1: int) -> None:
    """
    :param int_1: Input number
    :return: a + aa + aaa + aaaa
    """
    result = 0 
    for i in range(4): # 修改range中的值可以随意适应 a + aa + aaa + aaaa (+aaaaa)...
        for j in range(i+1):
            result += int_1 * 10 ** j
    return result
