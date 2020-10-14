"""
Copyright(C), ZYTC
File name: conftest.py
Author: lixc
Version: 0.1
Date: 2020-09-22
Description: 全局共享
"""

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

