"""
Copyright(C), ZYTC
File name: test_001_cpu.py
Author: lixc
Version: 0.2
Date: 2020-10-12
Description: Test case for memory status.
Preset : 假设 插满内存，单根8G
"""

import os
import allure
import pytest
import subprocess


board_model = os.getenv("BOARD_MODEL")

if board_model == "N4210":
    memsize = "16G"
else:
    memsize = "31G"


@allure.feature("内存状态测试")
@allure.title("查看内存容量是否正确")
def test_mem_size():
    ret = subprocess.run(r"ansible {} -m shell -a 'free -h --si | grep Mem'".format(board_model), shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert memsize in ret.stdout

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/MEM", "test_004_MEM.py"])
