#!/home/soft/py3env/bin/python

import os
import pytest
import subprocess
from whiptail import Whiptail

w = Whiptail(width=60, height=10)

if os.getenv("MORE_INTERACTIVE"):
    w.title = "Welcome"
    w.msgbox("欢迎使用主板检测系统，请点击 '确认' 开始测试。")
    w.title = "主板型号"
    w.height = 15
    board_model = w.radiolist("请选择主板型号：", ["A8210", "A8211", "A8240", "A8245", "A82451", "A8246"])[0][0]
    w.title = "主板序列号"
    board_serial = w.inputbox("请输入主板序列号:", default=board_model)[0]
else:
    board_model = "A8240"
    board_serial = "A82402010xxx"

os.environ["BOARD_MODEL"] = board_model

top_dir = os.getcwd()

result_dir = top_dir + "/results/" + board_model + "/" + board_serial
report_dir = top_dir + "/reports/" + board_model + "/" + board_serial


def run_testcase():
    """执行测试用例"""
    pytest.main(["--alluredir={}".format(result_dir), "--host-pattern={}".format(board_model), "cases"])


def generate_report():
    """生成测试报告"""
    subprocess.run("allure generate {} -c -o {}".format(result_dir, report_dir), shell=True,
                   stdout=subprocess.PIPE, universal_newlines=True, check=True)
    """打开测试报告"""
    subprocess.run("allure open {}".format(report_dir), shell=True,
                   stdout=subprocess.PIPE, universal_newlines=True, check=True)


def post_run():
    """测试完成后的操作"""
    del os.environ["BOARD_MODEL"]


try:

    run_testcase()

    #generate_report()

finally:
    post_run()
