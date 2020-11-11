from scripts.phone_basic_operate import  Phone_Basic_Operate

class JJFW(Phone_Basic_Operate):
    def __init__(self):
        Phone_Basic_Operate.__init__(self)
    def __del__(self):
        Phone_Basic_Operate.__del__(self)

    def click_jjfw(self):
        # 点击交警服务标签
        xpath_jjfw_value = "//*[contains(@text,'交警服务')]"
        ele_jjfw=self.locate_element("xpath",xpath_jjfw_value)
        self.ele_tap(ele_jjfw)

        #长按交警服务头部
        xpath_jjfwtb_value="//*[contains(@text,'banner')]"
        ele_jjfwtb=self.locate_element("xpath",xpath_jjfwtb_value)
        self.ele_longpress(ele_jjfwtb,3000)

        #获取保存图片标签文本
        xpath_picture_value="//*[contains(@text,'保存图片')]"
        p_text=self.get_attriname("xpath",xpath_picture_value,"text")

        return p_text
        # p_text2 = self.get_attriname("xpath", xpath_picture_value, "name")
        # p_text3 = self.get_attriname("xpath", xpath_picture_value, "className")
        # p_text4 = self.get_attriname("xpath", xpath_picture_value, "resourceId")



