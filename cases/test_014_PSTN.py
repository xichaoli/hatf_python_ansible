"""
Copyright(C), ZYTC
File name: test_001_cpu.py
Author: lixc
Version: 0.1
Date: 2020-11-18
Description: Test case for PSTN model.
"""

import os
import allure
import pytest
import subprocess


board_model = os.getenv("BOARD_MODEL")


@allure.feature("内存状态测试")
@allure.title("查看内存容量是否正确")
@pytest.mark.skipif(board_model != "A8245", reason="目前只有A8245型号产品使用了pstn模块")
def test_pstn_stat():
    ret = subprocess.run(r"ansible {} -m shell -a 'echo AT > /dev/ttyUSB2; head -n 5 /dev/ttyUSB2'".format(board_model), 
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "OK" in ret.stdout, "PSTN模块状态不正确，请reset系统后再试一次！"

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/pstn", "test_014_PSTN.py"])
