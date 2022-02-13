def str_join(seq: tuple) -> tuple:
    """
    :param seq: The source tuple
    :return: a tuple contain two str after jion
    """
    str_1 = "-"
    str_2 = ""
    return str_1.join(seq), str_2.join(seq)
