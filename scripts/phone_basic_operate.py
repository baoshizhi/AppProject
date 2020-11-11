#encoding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import base64
import time
import os
import codecs



# 获取手机基本信息
def get_phonemsg():
    # 获取设备号
    devices = os.system('adb devices')
    # 获取应用包名及启动名，需事先手工启动再获取
    app_message = os.system('adb shell dumpsys window windows | findstr mFocusedApp')

class Phone_Basic_Operate():
    def __init__(self):
        # 定义手机设备启动参数,字典型数据
        desired_caps = {}
        # 设备系统名
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion']='9'#如果不清楚可不定义该参数，但千万不要传错
        # 设备号
        desired_caps['deviceName'] = '8CYNW19912004879'
        # 应用包名
        appPackage = "com.digitalchina.mobile.dfhfz1"
        desired_caps['appPackage'] = appPackage
        # 应用启动名
        appActivity = 'com.systoon.toon.user.login.view.WelcomeActivity'
        desired_caps['appActivity'] = appActivity

        #防止APP每次启动时都需要重新登录
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False

        desired_caps['unicodeKeyboard'] = True  # unicode设置(允许中文输入)
        desired_caps['resetKeyboard'] = True  # 键盘设置(允许中文输入)
        desired_caps['autoGrantPermissions'] = True  # 自动决定获取安装app需要的权限
        # 声明手机驱动对象,http://127.0.0.1:4723为appium自动工具的启动地址及端口
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def __del__(self):
        self.driver_quit()

    def driver_quit(self):
        self.driver.quit()

    #根据不同的定位方式进行单个元素的定位
    def locate_element(self,locate_type,value):
        '''
        :param locate_type: 定位类型 如 id,class,xpath 三种定位类型
        :param value: 元素定位值 如xpath路径的值  //*[@content-desc="外卖"]
        :return:

        value='name' 返回content-desc / text属性值
  		value='text' 返回text的属性值
		value='className' 返回 class属性值，只有 API=>18 才能支持
		value='resourceId' 返回 resource-id属性值，只有 API=>18 才能支持
        '''
        el=None
        if locate_type=="id":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element_by_id(value))
            #el=self.driver.find_element_by_id(value)
        elif locate_type=="name":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element_by_name(value))


        elif locate_type=="class":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element_by_class_name(value))
            #el=self.driver.find_element_by_class_name(value)
        elif locate_type=="xpath":
            #显式等待，每0.5秒轮询一次，超时10秒抛出错误
            #value="//*[contains(@text,'交通出行')"]

            el=WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_xpath(value))
            #el=self.driver.find_element_by_xpath(value)
        return el

    # 根据不同的定位方式进行多个元素的定位
    def locate_more_elements(self, locate_type, value):

        el = None
        if locate_type == "id":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements_by_id(value))
            # el=self.driver.find_elements_by_id(value)
        elif locate_type == "name":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_elements_by_name(value))
            #el = self.driver.find_elements_by_name(value)

        elif locate_type == "class":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            el = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements_by_class_name(value))
            # el=self.driver.find_elements_by_class_name(value)
        elif locate_type == "xpath":
            # 显式等待，每0.5秒轮询一次，超时10秒抛出错误
            # value="//*[contains(@text,'交通出行')"]
            el = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements_by_xpath(value))
            # el=self.driver.find_elements_by_xpath(value)
        return el

    #获取元素坐标
    def get_positon(self,locate_type,value):
        el=self.locate_element(locate_type,value)
        positon=el.location
        print("元素坐标:",positon)
        return  positon

    #获取元素属性名
    def get_attriname(self,loate_type,locate_value,attribute_type):
        """
        :param loate_type: 元素定位方式
        :param locate_value: 元素定位值
        :param attribute_type: 属性类型如
           value='name' 返回content-desc / text属性值
  		   value='text' 返回text的属性值
		   value='className' 返回 class属性值，只有 API=>18 才能支持
		   value='resourceId' 返回 resource-id属性值，只有 API=>18 才能支持
        :return:
        """
        el=self.locate_element(loate_type,locate_value)
        attriname_text=el.get_attribute(attribute_type)
        print("属性类型:%s,属性值:%s"%(attribute_type,attriname_text))
        return attriname_text

    #获取截图
    def get_screen(self):
        #img_folder=os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) +'//screenshots'
        img_folder="E:\\AppProject\\screenshot" +'//screenshots'
        screentime=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_save_path=img_folder+ screentime +'.png'
        self.driver.get_screenshot_as_file(screen_save_path)


    #点击元素
    def click(self,locate_type,value):
        el=self.locate_element(locate_type,value)
        el.click()

    #元素文本录入
    def input(self,locate_type,value,text):
        el=self.locate_element(locate_type,value)
        el.clear()
        el.send_keys(text)

    #获取打印手机时间
    def get_time(self):
        phone_time=self.driver.device_time
        print(phone_time)
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        return phone_time

    # 获取打印手机分辨率
    def get_size(self):
        window_size= self.driver.get_window_size()
        width_size=window_size.get("width")
        height_size=window_size.get("height")
        print("Width:",width_size)
        print("Height:",height_size)
        return window_size

    #从一个坐标滑动到另外一个坐标,持续时间的单位为毫秒
    def ele_swip(self,start_x, start_y, end_x, end_y,duration=None):
        self.driver.swipe(start_x,start_y,end_x,end_y,duration)

    #从一个元素滑动到另外一个元素，直到页面自己停止
    def ele_scroll(self,origin_el, destination_el,duration=None):
        self.driver.scroll(origin_el,destination_el,duration)

    #从一个元素拖动到另外一个元素处放开(有可能是点击的效果？)
    def ele_dragdrop(self,origin_el,destination_el):
        self.driver.drag_and_drop(origin_el,destination_el)

    #长按某个元素，时间单位为毫秒
    def ele_longpress(self,press_ele,duration_time=None):
        TouchAction(self.driver).long_press(press_ele,duration=duration_time).perform().release()

    #点击某个元素
    def ele_tap(self,tap_ele):
        TouchAction(self.driver).tap(tap_ele).perform().release()



    #模拟粘贴 v:50 ctrl:4096
    def ctrlv(self):
        self.driver.keyevent(50,4096)

    #将应用置于后台一段时间
    def background(self,seconds_n):
        self.driver.background_app(seconds_n)

    #打开通知栏
    def open_notifications(self):
        self.driver.open_notifications()
    #点击home键
    def back_home(self):
        self.driver.keyevent(3)
    #获取手机当前网络
    def get_network(self):
        network=self.driver.network_connection
        print(network)
        return network




    #将电脑端文件发送到手机目录下
    #pc_data_path="D:\\AppProject\\data_file\\wuhan.txt"
    #phone_path="/sdcard/wuhan14.txt"
    def push_to_phone(self,pc_data_path,phone_path):
        #读取文件路径中的数据
        with open(pc_data_path,encoding='utf-8') as f:
            pc_data=f.read()
            #print(pc_data)
        #转化为utf-8格式
        pc_data_utf8=pc_data.encode('utf-8')
        #转化为b64格式
        pc_data_b64=str(base64.b64encode(pc_data_utf8),'utf-8')
        self.driver.push_file(phone_path,pc_data_b64)

    #从手机上拉取文件
    def pull_from_phone(self,phone_path):
        #返回的是b64格式数据
        data_b64=self.driver.pull_file(phone_path)

        #解码b64格式数据
        data_b64decode = base64.b64decode(data_b64.encode('utf-8'))
        data=str(data_b64decode,'utf-8')
        print("pull:\n",data)
    #
    # def operate(self):
    #     # 判断是否安装app
    #     print(self.driver.is_app_installed(self.appPackage))
    #     app_path = "D:\\AppProject\\AppPackage\\ZUOYEBAN12.9.0.apk"
    #     self.driver.install_app(app_path)
    #     #关闭当前操作的app，但不关闭driver
    #     self.driver.close_app()
    #
    #     #关闭驱动对象
    #     self.driver.quit()
    #     #启动应用
    #     self.driver.start_activity(self.appPackage,self.appActivity)

if __name__ == '__main__':
    #获取手机应用基本信息
    #get_msg=get_phonemsg()

    PBOperate=Phone_Basic_Operate()

    #点击【交通出行】
    xpath_value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView"
    ele=PBOperate.locate_element("xpath",xpath_value)
    print(ele.location())
    #PBOperate.click("xpath",xpath_value)

    #PBOperate.click("class","android.view.View")
    #PBOperate.click('xpath','//*[@content-desc="外卖"]')
    time.sleep(2)
    #PBOperate.click('xpath','//*[contains(@content-desc,"外卖")]')
    #PBOperate.click('xpath','//android.view.View[@content-desc="外卖"]')
    time.sleep(3)
    #PBOperate.click('id','//*[@resource-id="com.sankuai.meituan:id/gridview_major_category"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]') #点击美食









