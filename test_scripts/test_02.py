import pytest
class Test_aaa():
    def setup(self):
        print("--setup---")
    def setup_class(self):
        print("--1setup_class--")
    def teardown(self):
        print("---teardown---")
    def teardown_class(self):
        print("--1teardown_class--")

    def test_001(self):
        assert True

    def test_002(self):
        assert False

    def test_003(self):
        assert True

class Test_bbb():
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_004(self):
        assert True
    def test_005(self):
        assert True
    def test_006(self,init_data2):
        assert True



