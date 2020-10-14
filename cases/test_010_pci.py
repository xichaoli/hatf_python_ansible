"""
Copyright(C), ZYTC
File name: test_010_PCIe.py
Author: lixc
Version: 0.1
Date: 2020-10-14
Description: Test case for PCIe slots.
BUGS: 忽略了同一张卡不同网口状态不一致的情况
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail
from pytest_dependency import depends


board_model = os.getenv("BOARD_MODEL")
if board_model == "A8210":
    device_list = ["03:00", "0b:00", "0001:22:00"]
else: # A8240
    device_list = ["03:00", "0b:00", "0001:22:00", "0001:25:00"]


@pytest.fixture(scope="module", params=device_list)
def plug_into_pcie_card(request):
   """测试前确认所需设备是否插好"""
   device_vendor = request.param
   w = Whiptail(width=60, height=10, title="请确认")

   if device_vendor == "03:00":
        device = "横插X710"
   elif device_vendor == "0b:00":
        device = "丽华两口X710"
   elif device_vendor == "0001:22:00":
        device = "LR-LINK 四口X710"
   else:
        device = "FP068E 四口X710"

   w.msgbox("请确认测试用pcie卡 {} 已正确插入".format(device))

   return device_vendor


@allure.feature("PCIe 插槽测试")
@allure.title("查看PCIe卡是否被正确识别")
@pytest.mark.dependency()
def test_pcie_card_identification(plug_into_pcie_card):
    ret = subprocess.run("ansible {} -m shell -a 'lspci -n -s {}'".format(board_model, plug_into_pcie_card),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "8086:1572" in ret.stdout or "8086:1581" in ret.stdout , "PCIe卡{}识别不正确，请做进一步检查".format(plug_into_pcie_card)


@allure.feature("PCIe 插槽测试")
@allure.title("查看PCIe卡连接状态是否为预期")
@pytest.mark.dependency()
def test_usb_protocol(request, plug_into_pcie_card):
    depends(request, ["test_pcie_card_identification[{}]".format(plug_into_pcie_card)])
    ret = subprocess.run("ansible {} -m shell -a 'lspci -n -s {} -vv | grep LnkSta:'".format(board_model, plug_into_pcie_card),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "Speed 8GT/s, Width x8" in ret.stdout, "PCIe卡{}连接状态不正确，请做进一步检查".format(plug_into_pcie_card)


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/PCIe", "test_010_PCIe.py"])