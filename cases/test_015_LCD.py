"""
Copyright(C), ZYTC
File name: test_015_LCD.py
Author: lixc
Version: 0.1
Date: 2020-11-24
Description: Test case for LCD.
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail


board_model = os.getenv("BOARD_MODEL")


@allure.feature("液晶屏状态测试")
@allure.title("查看液晶屏显示是否正确")
@pytest.mark.skipif(board_model != "A82451", reason="目前只有A82451型号产品使用了LCD液晶屏")
def test_lcd_stat():
    subprocess.run(r"ansible {} -m shell -a 'nohup dwin_lcd 0 &'".format(board_model), 
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=15, title="LCD 显示")
    ret = w.yesno("LCD显示屏在设备启动时显示 '设备启动中...'。\
            执行测试用例后能否显示设备IP地址等信息？\
            显示屏每10秒钟刷新一次。", default="no")
    assert not ret, "液晶屏显示不正确"

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/lcd", "test_015_lcd.py"])
