"""
Copyright(C), ZYTC
File name: test_006_beep.py
Author: lixc
Version: 0.1
Date: 2020-10-14
Description: Test case for poweroff.
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail

board_model = os.getenv("BOARD_MODEL")

@allure.feature("关机测试")
@allure.title("查看能否控制设备关机")
@pytest.mark.skip(reason="暂不执行")
def test_shutdown():
    subprocess.run("ansible {} -m shell -a 'shutdown -h now'".format(board_model), shell=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认系统是否关机成功", default="no")
    assert not ret, "关机功能测试失败，请做进一步检测"


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/RTC", "test_006_beep.py"])
