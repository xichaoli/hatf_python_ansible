"""
Copyright(C), ZYTC
File name: test_004_rtc.py
Author: lixc
Version: 0.1
Date: 2020-09-22
Description: Test case for RTC.
"""

import allure
import pytest
import subprocess

@allure.feature("时钟测试")
@allure.title("查看rtc设备是否存正确写入")
def test_rtc_write(get_pwd):
    ret = subprocess.run("echo {}| sudo -S hwclock -w".format(get_pwd), shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert 0 == ret.returncode

@allure.title("查看rtc设备是否存正确读取")
def test_rtc_read(get_pwd):
    ret = subprocess.run("echo {}| sudo -S hwclock -r".format(get_pwd), shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert 0 == ret.returncode

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/RTC", "test_004_rtc.py"])
