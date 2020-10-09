#atf
使用步骤：
1. 如使用了python 虚拟环境，请先进入虚拟环境。
  user@sw-uos:~$ . py3env/bin/activate

2. 开始测试
  (py3env) user@sw-uos:~/atf$ python run.py
  然后根据提示进行操作。完成后会在reports目录下的 主板型号/主板序列号 目录里生成测试报告。

3. 查看测试报告
  需要在图形界面下。
  使用allure open 命令通过浏览器展示测试详情。
  示例如下：
  (py3env) user@sw-uos:~/atf$ allure open reports/A8210/A82102007001/

