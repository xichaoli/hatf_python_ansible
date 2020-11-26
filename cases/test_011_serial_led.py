"""
Copyright(C), ZYTC
File name: test_011_serial_led.py
Author: lixc
Version: 0.1
Date: 2020-11-12
Description: Test case for serial led.
"""

import os
import allure
import pytest
import subprocess
from whiptail import Whiptail

board_model = os.getenv("BOARD_MODEL")

@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制电源灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_power():
    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认电源灯是否长亮？", default="no")
    assert not ret, "电源灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制故障灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_fail():
    subprocess.run("ansible {} -m shell -a 'serled 0 0 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认故障灯是否长亮？", default="yes")
    assert ret, "故障灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制故障灯熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_down_fail():
    subprocess.run("ansible {} -m shell -a 'serled 0 0 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认故障灯是否熄灭？", default="yes")
    assert ret, "故障灯没有熄灭，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制报警灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_alarm():
    subprocess.run("ansible {} -m shell -a 'serled 0 1 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认报警灯是否长亮？", default="yes")
    assert ret, "报警灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制报警灯熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_down_alarm():
    subprocess.run("ansible {} -m shell -a 'serled 0 1 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认报警灯是否熄灭？", default="yes")
    assert ret, "报警灯没有熄灭，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网1灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_internal1():
    subprocess.run("ansible {} -m shell -a 'serled 2 7 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网1灯是否长亮？", default="yes")
    assert ret, "内网1灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网1灯熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_down_internal1():
    subprocess.run("ansible {} -m shell -a 'serled 2 7 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网1灯是否熄灭？", default="yes")
    assert ret, "内网1灯没有熄灭，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网2灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_internal2():
    subprocess.run("ansible {} -m shell -a 'serled 2 6 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网2灯是否长亮？", default="yes")
    assert ret, "内网2灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网2灯熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_down_internal2():
    subprocess.run("ansible {} -m shell -a 'serled 2 6 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网2灯是否熄灭？", default="yes")
    assert ret, "内网2灯没有熄灭，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网3灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_internal3():
    subprocess.run("ansible {} -m shell -a 'serled 2 5 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网3灯是否长亮？", default="yes")
    assert ret, "内网3灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网灯3熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_internal3():
    subprocess.run("ansible {} -m shell -a 'serled 2 5 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网3灯是否熄灭？", default="yes")
    assert ret, "内网3灯没有熄灭，请做进一步检查"

@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网4灯长亮")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_up_internal4():
    subprocess.run("ansible {} -m shell -a 'serled 2 4 1'".format(board_model), shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网4灯是否长亮？", default="yes")
    assert ret, "内网4灯不是长亮，请做进一步检查"


@allure.feature("串口LED灯板测试")
@allure.title("查看能否控制内网4灯熄灭")
@pytest.mark.skipif(board_model != "A8211", reason="目前只有A8211型号产品使用了串口led灯板")
def test_beep_down_internal4():
    subprocess.run("ansible {} -m shell -a 'serled 2 4 0'".format(board_model), shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)

    w = Whiptail(width=40, height=10, title="请确认")
    ret = w.yesno("请确认内网4灯是否熄灭？", default="yes")
    assert ret, "内网4灯没有熄灭，请做进一步检查"


if __name__ == "__main__":
    pytest.main(["--alluredir", "results/LED", "test_011_serial_led.py"])
