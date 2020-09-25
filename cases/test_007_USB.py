"""
Copyright(C), ZYTC
File name: test_001_USB.py
Author: lixc
Version: 0.1
Date: 2020-09-25
Description: Test case for USB ports.
"""

import allure
import pytest
import subprocess
from whiptail import Whiptail
from pytest_dependency import depends

@pytest.fixture(scope="module")
def plug_into_usb():
   """测试前确认所需设备是否插好"""
   w = Whiptail(width=60, height=10, title="需确认")
   w.msgbox("请确认测试U盘已插入。下面的测试命令使用的设备ID号为 0781:5590，对应的测试U盘型号为Sandisk 。")

@allure.feature("USB端口测试")
@allure.title("查看U盘是否被正确识别")
@pytest.mark.dependency()
def test_usb_identification(plug_into_usb):
    ret = subprocess.run("lsusb -d 0781:5590", shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert 0 == ret.returncode

@pytest.mark.dependency()
@allure.title("查看USB接口所遵循的协议版本号是否为预期")
def test_usb_protocol(request, plug_into_usb):
    depends(request, ["test_usb_identification"])
    ret = subprocess.run("lsusb -d 0781:5590 -v | grep bcdUSB", shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "2.10" in ret.stdout or "3.00" in ret.stdout

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/USB", "test_007_USB.py"])
