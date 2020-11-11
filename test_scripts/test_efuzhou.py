import pytest
#from scripts.jjfw import JJFW
from scripts.pageobject import PageObject
import time


class Test_efuzhou():
    def setup_class(self):
        # 实例化一个JJFW类
        self.JJFW=PageObject().Rev_JJFW()
    def teardown_class(self):
        self.JJFW.__del__()

    def test_jjfw(self):
        p_text=self.JJFW.click_jjfw()
        #出错保存截图
        if p_text!="保存图片":
            self.JJFW.get_screen()
        assert p_text=="保存图片","长按交警服务头部图片未弹出保存图片提示"










