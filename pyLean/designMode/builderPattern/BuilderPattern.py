# -*- encoding:utf-8 -*-
"""
@File   :BuilderPattern.py
@Time   :2020/10/21 8:38
@Author :Chen
@Software:PyCharm
"""


# 具体产品对象
class Menu:
    Menu_A = []
    Menu_B = []
    Menu_C = []

    def set_MenuA(self, item):
        self.Menu_A.append(item)

    def set_MenuB(self, item):
        self.Menu_B.append(item)

    def set_MenuC(self, item):
        self.Menu_C.append(item)

    def get_MenuA(self):
        return self.Menu_A

    def get_MenuB(self):
        return self.Menu_B

    def get_MenuC(self):
        return self.Menu_C

# Builder（抽象建造者）
# 创建一个Product对象的各个部件指定的抽象接口。
class Product:
    product = Menu()

    def build_hanbao(self):
        pass

    def build_jiroujuan(self):
        pass

    def build_kele(self):
        pass

    def build_shutiao(self):
        pass


# ConcreteBuilder（具体建造者）
# 实现抽象接口，构建和装配各个部件。
# 套餐C
class product_C(Product):
    type = "C"

    def __init__(self):
        self.hanbao = '大排牛肉双层沙拉汉堡'
        self.jiroujuan = '麻辣鸡肉卷'
        self.kele = '冰镇大杯可乐'
        self.shutiao = '双份夹心薯条'

    def build_hanbao(self):
        self.product.set_MenuC(self.hanbao)

    def build_jiroujuan(self):
        self.product.set_MenuC(self.jiroujuan)

    def build_kele(self):
        self.product.set_MenuC(self.kele)

    def build_shutiao(self):
        self.product.set_MenuC(self.shutiao)

    def getType(self):
        return type


# 套餐A
class product_A(Product):
    type = "A"

    def __init__(self):
        self.kele = "可乐"
        self.hanbao = "汉堡"

    def build_hanbao(self):
        self.product.set_MenuA(self.hanbao)

    def build_kele(self):
        self.product.set_MenuA(self.kele)

    def getType(self):
        return type


# 套餐B
class product_B(Product):
    type = "B"

    def __init__(self):
        self.kele = "可乐"
        self.jiroujuan = "鸡肉卷"
        self.shutiao = "薯条"

    def build_shutiao(self):
        self.product.set_MenuB(self.shutiao)

    def build_jiroujuan(self):
        self.product.set_MenuB(self.jiroujuan)

    def build_kele(self):
        self.product.set_MenuB(self.kele)

    def getType(self):
        return type


# Director（指挥者）
class Make:
    def __init__(self):
        self.builder = None

    def build_product(self, builder):
        self.builder = builder
        print(builder.type)
        if builder.type == "A":
            [step() for step in (builder.build_hanbao,
                                 builder.build_kele)]
        if builder.type == "B":
            [step() for step in (builder.build_shutiao,
                                 builder.build_jiroujuan,
                                 builder.build_kele)]
        if builder.type == "C":
            [step() for step in (builder.build_hanbao,
                                 builder.build_kele,
                                 builder.build_shutiao,
                                 builder.build_jiroujuan)]


# 不同类型选择
def validate_style(builders):
    global valid_input
    try:
        print('套餐A：汉堡、可乐' + '\n'
                            '套装B：薯条、鸡肉卷、可乐' + '\n'
              '套餐C：汉堡、鸡肉卷、可乐、薯条')
        product_style = input('请输入您的选择：')
        builder = builders[product_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, 没有这个套餐，请重新选择。')
        return (False, None)
    return (True, builder, product_style)


# 主函数
def main():
    builders = dict(A=product_A, B=product_B, C=product_C)
    valid_input = False
    while not valid_input:
        valid_input, builder, product_style = validate_style(builders)
    Waiter = Make()
    Waiter.build_product(builder)
    if product_style == "A":
        print(builder.product.get_MenuA())
    elif product_style == "B":
        print(builder.product.get_MenuB())
    else:
        print(builder.product.get_MenuC())


if __name__ == "__main__":
    main()
