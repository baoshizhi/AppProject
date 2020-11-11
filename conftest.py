import pytest

@pytest.fixture(scope="session")
def init_data2():
    print("---初始化数据init_data2---")

