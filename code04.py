# 写一个函数，判断是不是奇数
def isOdd(num):
    """
    判断这个数是不是奇数
    :param num: num
    :return: True False
    :param num:
    :return:
    """
    if num % 2 == 0:
        return False
    else:
        return True


print(isOdd(56))
print(isOdd(89))
