import pytest

@pytest.fixture(params=[1,2,3])
def init_data(request):
    return request.param

class Test_aa():
    def setup(self):
        pass
    def teardown(self):
        pass

    def test_01(self,init_data):
        print("---test_01---")
        assert init_data==2

