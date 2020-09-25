"""
Copyright(C), ZYTC
File name: test_001_cpu.py
Author: lixc
Version: 0.1
Date: 2020-09-21
Description: Test case for memory status.
"""

import allure
import pytest
import subprocess

@allure.feature("内存状态测试")
@allure.title("查看内存容量是否正确")
def test_cpu_num():
    ret = subprocess.run("head -1 /proc/meminfo", shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "31587056" in ret.stdout

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/MEM", "test_002_MEM.py"])
