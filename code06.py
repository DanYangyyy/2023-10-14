#全局变量 局部变量

x = 10


# def test():
#     x = 20
#     print(f'局部变量x = {x}')

def test():
    global x
    x = 20
    print(f'局部变量 x = {x}')


test()
print(f'全局变量 x = {x}')
