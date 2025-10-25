def isOdd(param):
    # 首先判断参数是否为整数类型
    if isinstance(param, int):
        # 如果是整数，判断是否为奇数（奇数是不能被 2 整除的整数）
        return param % 2 != 0
    # 如果参数不是整数，直接返回 False
    else:
        return False
