import pytest

@pytest.fixture()
def init_data():
    print("\n--初始化数据--initdata--")
    with open("./data.txt","w") as f:
        f.write("11232输入初始化数据")

@pytest.mark.usefixtures("init_data")
class Test_aa():
    def setup(self):
        pass
    def teardown(self):
        pass

    @pytest.mark.run(order=2)
    def test_01(self):
        print("--test_01--")
        assert True

    @pytest.mark.run(order=1)
    def test_02(self):
        print("--test_02--")
        assert True

    # @pytest.mark.run(order=3)
    # def test_03(self,init_data): #运行test_03函数之前先调用标记函数init_data
    #     with open("./data.txt","r") as f:
    #         print("\n--test_03--\n")
    #         read_data=f.read() #只能读取一次，再读的话读取出的数据会为空
    #         print("输出数据:",read_data)
    #     assert read_data=="11232输入初始化数据","读取失败"


    @pytest.mark.run(order=-3)
    def test_04(self):
        print("--test_04--")
        assert True

    @pytest.mark.run(order=-4)
    def test_05(self):
        print("--test_05--")
        assert True

    @pytest.mark.run(order=0)
    def test_06(self):
        print("--test_06--")
        assert True

    def test_07(self):
        print("--test_07--")
        assert True




