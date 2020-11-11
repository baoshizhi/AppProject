import pytest

def nameage_list():
    return [('xiaobao1', 20), ('xiaobao2', 21), ('xiaobao3', 22)]

class Test_para():
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    # @pytest.mark.parametrize("name",["xiaobao1","xiaobao2","xiaobao3"])
    # def test_pa01(self,name):
    #     assert name =="xiaobao1"
    @pytest.mark.parametrize("name,age",nameage_list())
    def test_pa02(self,name,age):
        print("name:%s,age:%s" %(name,age))
        # assert name =="xiaobao2"
        # assert age ==21