"""
Copyright(C), ZYTC
File name: test_001_cpu.py
Author: lixc
Version: 0.2
Date: 2020-10-12
Description: Test case for memory status.
"""

import os
import allure
import pytest
import subprocess


board_model = os.getenv("BOARD_MODEL")

if board_model == "N4210":
    memsize = 16221570
else:
    memsize = 64886280


@allure.feature("内存状态测试")
@allure.title("查看内存容量是否正确")
def test_cpu_num():
    ret = subprocess.run("ansible {} -m shell -a 'head -1 /proc/meminfo'".format(board_model), shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert str(memsize) in ret.stdout

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/MEM", "test_004_MEM.py"])
