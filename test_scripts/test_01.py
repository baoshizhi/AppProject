import pytest
import os
class Test_aa():
    def setup(self):
        print("--setup---")
    def setup_class(self):
        print("--1setup_class--")
    def teardown(self):
        print("---teardown---")
    def teardown_class(self):
        print("--1teardown_class--")

    def test_01(self,init_data2):
        assert True

    def test_02(self):
        assert False

    def test_03(self):
        assert True

class Test_bb():
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_04(self):
        assert True
    def test_05(self):
        assert True
    # def test_06(self,init_data2):
    #     assert True


if __name__ == '__main__':
    print("2222222222222222")
    os.system("pytest")
    T=None
    print(T)





