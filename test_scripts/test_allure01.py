import pytest,allure

@allure.feature("测试类Test_t01功能说明---")
class Test_t01():
    def setup_class(self):
        pass
    def teardown_class(self):
        pass


    @allure.story('--测试用例功能划分01--')
    @allure.title("--测试用例标题title01--")
    @allure.description("测试用例描述test01")
    @allure.step('--步骤step01---')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("http://www.baidu.com","测试用例链接")
    @allure.issue("http://www.hao123.com","测试bug地址")
    def test_01(self):
        assert True

    @allure.story('--测试用例功能划分01--')
    @allure.title("--测试用例标题title02--")
    @allure.description("测试用例描述test02")
    @allure.step('--步骤step02---')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_02(self):
        assert True

    @allure.story('--测试用例功能划分02--')
    @allure.title("--测试用例标题title03--")
    @allure.description("测试用例描述test03")
    @allure.step('--步骤step03---')
    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        assert False

    @allure.story('--测试用例功能划分02--')
    @allure.title("--测试用例标题title04--")
    @allure.description("测试用例描述test04")
    @allure.step('--步骤step04---')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_04(self):
        assert True



# @allure.feature("--类别称Test_t02---")
# class Test_t02():
#     def setup_class(self):
#         pass
#     def teardown_class(self):
#         pass
#
#
#     @allure.story('--story_test01--')
#     @allure.title("--测试用例标题title01--")
#     @allure.description("测试用例描述test01")
#     @allure.step('--步骤step01---')
#     @allure.severity(allure.severity_level.TRIVIAL)
#     def test_01(self):
#         assert False
#
#     @allure.story('--story_test02--')
#     @allure.title("--测试用例标题title02--")
#     @allure.description("测试用例描述test02")
#     @allure.step('--步骤step02---')
#     def test_02(self):
#         assert True

if __name__ == '__main__':
    pytest.main(["-s","-q","-v",r"--alluredir=../report/allure_xml_report", "test_allure01.py"])