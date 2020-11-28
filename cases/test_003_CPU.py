"""
Copyright(C), ZYTC
File name: test_003_CPU.py
Author: lixc
Version: 0.2
Date: 2020-10-12
Description: Test case for CPU status.
"""

import os
import allure
import pytest
import subprocess


board_model = os.getenv("BOARD_MODEL")
if board_model == "N4210":
    cpu_num = 4
    cpu_freq = 1400.00
else:
    cpu_num = 16
    cpu_freq = 1600.00


@allure.feature("CPU状态测试")
@allure.title("查看CPU核心数量是否正确")
def test_cpu_num():
    ret = subprocess.run(r"ansible {} -m shell -a 'lscpu | grep ^CPU\(s\):'".format(board_model),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert str(cpu_num) in ret.stdout


@allure.feature("CPU状态测试")
@allure.title("查看是否有CPU核心离线")
def test_cpu_offline():
    ret = subprocess.run(r"ansible {} -m shell -a 'lscpu'".format(board_model),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert "Off-line" not in ret.stdout, "有CPU核心离线，请使用 lscpu -e -c 做进一步检测"


@allure.feature("CPU状态测试")
@allure.title("查看CPU主频是否正确")
def test_cpu_freq():
    ret = subprocess.run("ansible {} -m shell -a 'grep frequency /proc/cpuinfo'".format(board_model),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    assert str(cpu_freq) in ret.stdout


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/CPU", "test_003_CPU.py"])

