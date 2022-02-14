def list_expression(list_1: list, list_2: list):
    '''
    :param list_1: Input list_1
    :param list_2: Input list_2
    :return: nothing
    '''
    # 两个列表的每个值进行相乘,相加,固定位置相乘
    # 使用推倒式来进行 [x for x in ]
    print([i * j for i in list_1 for j in list_2])
    print([i + j for i in list_1 for j in list_2])
    print([list_1[i] * list_2[i] for i in range(len(list_1))])
