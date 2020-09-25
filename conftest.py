"""
Copyright(C), ZYTC
File name: conftest.py
Author: lixc
Version: 0.1
Date: 2020-09-22
Description: 全局共享
"""

import pytest

sudo_pwd = ["user123"]

@pytest.fixture(params=sudo_pwd)
def get_pwd(request):
    return request.param

