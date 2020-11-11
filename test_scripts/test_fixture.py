import pytest

#@pytest.fixture(scope="module")
@pytest.fixture(scope="class")
def init_data():
    print("---初始化数据init_data---")


@pytest.mark.usefixtures("init_data")
class Test_t01():
    def setup(self):
        print("---setup---")
        pass
    def teardown(self):
        pass

    #@pytest.mark.usefixtures("init_data")
    def test_f01(self):
        print("---test_f01---")

    def test_f02(self):
        print("---test_f02----")

@pytest.mark.usefixtures("init_data")
class Test_t02():
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_f03(self):
        print("---test_f03---")

    def test_f04(self):
        print("---test_f04----")