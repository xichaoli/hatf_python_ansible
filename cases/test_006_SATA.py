"""
Copyright(C), ZYTC
File name: test_001_USB.py
Author: lixc
Version: 0.1
Date: 2020-09-24
Description: Test case for SATA ports.
"""

import allure
import pytest
import subprocess
from whiptail import Whiptail

@pytest.fixture()
def plug_into_harddisk():
   """测试前确认所需设备是否插好"""
   w = Whiptail(width=60, height=10, title="需确认")
   w.msgbox("请确认设备型号为WD1004FBYZ-23YC 和 ST1000VX005-2EZ1 的测试硬盘已分别插入SATA1、SATA2口。")

@allure.feature("SATA 端口测试")
@allure.title("查看SATA口硬盘是否被正确识别")
def test_sata_identification(plug_into_harddisk):
    ret = subprocess.run("lsscsi", shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "WD1004FBYZ-23YC" in ret.stdout , "SATA1 口所接硬盘没有被正确识别"
    assert "ST1000VX005-2EZ1" in ret.stdout, "SATA2 口所接硬盘没有被正确识别"

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/SATA", "test_006_SATA.py"])
