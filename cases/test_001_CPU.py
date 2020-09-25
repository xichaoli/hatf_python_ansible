"""
Copyright(C), ZYTC
File name: test_001_cpu.py
Author: lixc
Version: 0.1
Date: 2020-09-21
Description: Test case for CPU status.
"""

import allure
import pytest
import subprocess

@allure.feature("CPU状态测试")
@allure.title("查看CPU核心数量是否正确")
def test_cpu_num():
    ret = subprocess.run(r"lscpu | grep ^CPU\(s\):", shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "16" in ret.stdout

@allure.title("查看CPU主频是否正确")
def test_cpu_freq():
    ret = subprocess.run(r"lscpu | grep CPU\ MHz:", shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "1600.00" in ret.stdout

if __name__ == "__main__":
    pytest.main(["--alluredir", "results/CPU", "test_001_cpu.py"])
