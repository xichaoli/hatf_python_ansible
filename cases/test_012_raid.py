"""
Copyright(C), ZYTC
File name: test_012_raid.py
Author: lixc
Version: 0.2
Date: 2020-11-26
Description: Test case for raid status.
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail

board_model = os.getenv("BOARD_MODEL")

@allure.feature("raid状态检测")
@allure.title("查看raid状态是否为raid1")
@pytest.mark.skipif(board_model != "A8211" and board_model != "A82451", reason="当前型号产品未使用或无需进行raid卡功能测试")
def test_raid_stat():
    ret = subprocess.run("ansible {} -m shell -a 'megacli -LDInfo -Lall -a0'".format(board_model), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "Primary-1, Secondary-0, RAID Level Qualifier-0" in ret.stdout, "raid状态不是raid1，请做进一步检测"


@allure.feature("raid状态检测")
@allure.title("查看raid磁盘是否已正确格式化为ext4")
@pytest.mark.skipif(board_model != "A8211" and board_model != "A82451", reason="当前型号产品未使用或无需进行raid卡功能测试")
def test_raid_format():
    ret = subprocess.run("ansible {} -m shell -a 'lsblk -f /dev/sdb'".format(board_model), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "ext4" in ret.stdout, "raid 1 分区格式不是ext4，请做进一步检测"


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/raid", "test_012_raid.py"])
