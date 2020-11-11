from scripts.jjfw import JJFW

class PageObject():
    def __init__(self):
        pass
    def __del__(self):
        pass

    #返回一个实例化的JJFW类供测试类调用
    def Rev_JJFW(self):
        return JJFW()
