"""
Copyright(C), ZYTC
File name: test_013_business.py
Author: lixc
Version: 0.1
Date: 2020-11-12
Description: Test case for business network ports.
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail
from pytest_dependency import depends

board_model = os.getenv("BOARD_MODEL")

if board_model == "A8211":
    port_list = ["enp3s0f0", "enp3s0f1", "enp3s0f2", "enp3s0f3"]
elif board_model == "A8246":
    port_list = ["enP1p36s0f0", "enP1p36s0f1", "enP1p36s0f2", "enP1p36s0f3"]
else:
    port_list = []


@pytest.fixture(scope="module", params=port_list)
def plug_into_cable(request):
    """测试前确认网线是否插好"""
    port = request.param
    if os.getenv("MORE_INTERACTIVE"): 
        w = Whiptail(width=60, height=10, title="请确认")
        w.msgbox("请确认业务网口 {} 的网线已接入千兆网络".format(port))
    return port


@allure.feature("业务网口测试")
@allure.title("查看业务网口能否正常通信")
@pytest.mark.dependency()
def test_interface_ping(plug_into_cable):
    if plug_into_cable == "enp3s0f0" or plug_into_cable == "enP1p36s0f0":
        dst_ip = "192.168.10.91"
    elif plug_into_cable == "enp3s0f1" or plug_into_cable == "enP1p36s0f1":
        dst_ip = "192.168.11.91"
    elif plug_into_cable == "enp3s0f2" or plug_into_cable == "enP1p36s0f2":
        dst_ip = "192.168.12.91"
    else:
        dst_ip = "192.168.13.91"

    ret = subprocess.run("ping -c 3 {}".format(dst_ip), shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=False)

    assert 0 == ret.returncode


@allure.feature("业务网口测试")
@allure.title("查看业务网口是否被正确识别")
@pytest.mark.dependency()
@pytest.mark.skipif(board_model == "A8210" or board_model == "A8240" or board_model == "A8245", reason="对于主板型号产品，不做业务网口的测试")
def test_interface_identification(request, plug_into_cable):
    if board_model == "A8211" or board_model == "A8246" or board_model == "A82451":
        drive = "igb"
    else:
        drive = "ixgbe"

    depends(request, ["test_interface_ping[{}]".format(plug_into_cable)])
    ret = subprocess.run("ansible {} -m shell -a 'ethtool -i {} | grep driver'".format(board_model, plug_into_cable),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    assert drive in ret.stdout


@allure.feature("业务网口测试")
@allure.title("查看业务网口的协商速率是否正确")
@pytest.mark.dependency()
def test_interface_stat(request, plug_into_cable):
    depends(request, ["test_interface_ping[{}]".format(plug_into_cable)])
    ret = subprocess.run("ansible {} -m shell -a 'ethtool {} | grep Speed:'".format(board_model, plug_into_cable),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    if board_model == "A8211" or board_model == "A8246" or board_model == "A82451":
        speed = "1000Mb/s"
    else:
        speed = "10000Mb/s"

    assert speed in ret.stdout


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/buiness", "test_013_buiness.py"])
