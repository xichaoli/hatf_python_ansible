import os
import pytest
import subprocess
from whiptail import Whiptail

w = Whiptail(width=60, height=10)

w.title = "Welcome"
w.msgbox("欢迎使用主板检测系统，请点击 '确认' 开始测试。")

w.title = "主板型号"
w.height = 14
board_model = w.radiolist("请选择主板型号：", ["A8210", "E8210", "A8240", "N8210", "N4210", "M4210"])[0][0]
os.environ["BOARD_MODEL"] = board_model

w.title = "主板序列号"
board_serial = w.inputbox("请输入主板序列号:", default=board_model)[0]
print(board_serial)

top_dir = os.getcwd()

result_dir = top_dir + "/results/" + board_model + "/" + board_serial
report_dir = top_dir + "/reports/" + board_model + "/" + board_serial

def select_testcase(model):
    """根据主板型号选择对应的测试用例"""
    src = top_dir + "/board/" + model
    dst = top_dir + "/cases_to_run"
    os.symlink(src, dst)

def run_testcase():
    """执行测试用例"""
    pytest.main(["--alluredir={}".format(result_dir), "--host-pattern={}".format(board_model), "cases_to_run"])

def generate_report():
    """生成测试报告"""
    subprocess.run("allure generate {} -c -o {}".format(result_dir, report_dir), shell=True,
                   stdout=subprocess.PIPE, universal_newlines=True, check=True)
    """打开测试报告"""
    subprocess.run("allure open {}".format(report_dir), shell=True,
                   stdout=subprocess.PIPE, universal_newlines=True, check=True)

def post_run():
    """测试完成后的操作"""
    os.unlink(top_dir + "/cases_to_run")
    del os.environ["BOARD_MODEL"]

try:
    select_testcase(board_model)

    run_testcase()

    generate_report()

finally:
    post_run()
