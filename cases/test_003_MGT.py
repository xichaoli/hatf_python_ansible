"""
Copyright(C), ZYTC
File name: test_001_MGT.py
Author: lixc
Version: 0.1
Date: 2020-09-22
Description: Test case for management network ports.
"""

import allure
import pytest
import subprocess
from whiptail import Whiptail
from pytest_dependency import depends


port_list = ["eth0", "eth1"]

@pytest.fixture(scope="module", params= port_list)
def plug_into_cable(request):
   """测试前确认网线是否插好"""
   port = request.param
   w = Whiptail(width=60, height=10, title="需确认")
   w.msgbox("请确认管理网口 {} 的网线已接入千兆网络".format(port))
   return port

@allure.feature("管理网口测试")
class TestGMT:
    @allure.title("查看管理网口是否被正确识别")
    @pytest.mark.dependency()
    def test_interface_identification(self, plug_into_cable):
        ret = subprocess.run("ethtool -i {} | grep driver".format(plug_into_cable), shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
        assert "st_gmac" in ret.stdout

    @allure.title("查看管理网口的协商速率是否正确")
    @pytest.mark.dependency()
    def test_interface_stat(self, request, plug_into_cable):
        depends(request, ["test_interface_identification[{}]".format(plug_into_cable)])
        ret = subprocess.run("ethtool {} | grep Speed:".format(plug_into_cable), shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, universal_newlines=True, check=True)
        assert "1000Mb/s" in ret.stdout

    @allure.title("查看管理网口能否正常通信")
    @pytest.mark.dependency()
    def test_interface_ping(self, request, plug_into_cable):
        depends(request, ["test_interface_identification[{}]".format(plug_into_cable)])
        if plug_into_cable == "eth0":
            dst_ip = "192.168.0.70"
        else:
            dst_ip = "192.168.1.70"

        ret = subprocess.run("ping -c 3 {}".format(dst_ip), shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, universal_newlines=True, check=True)
        assert 0 == ret.returncode

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/MGT", "test_003_MGT.py"])
