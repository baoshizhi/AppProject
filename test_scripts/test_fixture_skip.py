import pytest

def skip_reason():
    if 2 > 3:
        return True
    else:
        return False

class Test_cc():
    def setup_class(self):
        pass
    def teardown_class(self):
        pass
    @pytest.mark.skipif(skip_reason(),reason="--跳过执行的原因--")
    def test_101(self):
        print("--test_101--")
        assert True

    def test_102(self):
        print("--test_102--")
        assert True

