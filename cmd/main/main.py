import time
import unittest

from src.home.Test_home_update import TestHomeUpdate
from src.utils.config import init_test
from src.utils.logger import init_logger
from src.account.Test_login import TestLogin
from src.account.Test_register import TestRegister
from src.home.Test_home_newQuestions import TestHomeNewQuestion
from src.home.Test_home_paging import TestHomePaging
from src.home.Test_home_search import TestHomeSearch
from src.home.Test_home_delete import TestHomeDelete

if __name__ == '__main__':
    init_logger()
    init_test()
    time.sleep(1)
    while True:
        choice = input("请输入您需要测试的功能名称：")
        if choice == "login" or choice == "登录":
            print('开始执行登录自动化测试')
            suiteLogin = unittest.TestSuite()
            suiteLogin.addTest(TestLogin('test_login'))
            login = unittest.TextTestRunner()
            login.run(suiteLogin)
            time.sleep(0.3)
            print('login自动化测试完成')
            time.sleep(0.5)
        elif choice == "register" or choice == "注册":
            print('开始执行注册自动化测试')
            suiteRegister = unittest.TestSuite()
            suiteRegister.addTest(TestRegister('test_register'))
            register = unittest.TextTestRunner()
            register.run(suiteRegister)
            time.sleep(0.3)
            print("注册自动化测试完成")
            time.sleep(0.5)
        elif choice == "homeNewTest" or choice == "首页新增试题" or choice == "new":
            print('开始执行新增试题自动化测试')
            suiteNewTest = unittest.TestSuite()
            suiteNewTest.addTest(TestHomeNewQuestion('test_homeNewQuestion'))
            homeNewQuestion = unittest.TextTestRunner()
            homeNewQuestion.run(suiteNewTest)
            time.sleep(0.3)
            print("首页新增试题自动化测试完成")
            time.sleep(0.5)
        elif choice == "paging" or choice == "分页":
            print('开始执行分页自动化测试')
            suitePaging = unittest.TestSuite()
            suitePaging.addTest(TestHomePaging('test_homePaging'))
            homeNewQuestion = unittest.TextTestRunner()
            homeNewQuestion.run(suitePaging)
            time.sleep(0.3)
            print("分页自动化测试完成")
            time.sleep(0.5)
        elif choice == "search" or choice == "搜索":
            print("开始执行搜索自动化测试")
            suiteSearch = unittest.TestSuite()
            suiteSearch.addTest(TestHomeSearch('test_homeSearch'))
            homeSearch = unittest.TextTestRunner()
            homeSearch.run(suiteSearch)
            time.sleep(0.3)
            print("搜索自动化测试完成")
            time.sleep(0.5)
        elif choice == "delete" or choice == "删除":
            print("开始执行删除自动化测试")
            suiteDelete = unittest.TestSuite()
            suiteDelete.addTest(TestHomeDelete('test_homeDelete'))
            homeDelete = unittest.TextTestRunner()
            homeDelete.run(suiteDelete)
            time.sleep(0.3)
            print("搜索自动化测试完成")
            time.sleep(0.5)
        elif choice == "update" or choice == '修改':
            print("修改自动化测试开始")
            suiteUpdate = unittest.TestSuite()
            suiteUpdate.addTest(TestHomeUpdate('test_homeUpdate'))
            homeUpdate = unittest.TextTestRunner()
            homeUpdate.run(suiteUpdate)
            time.sleep(0.3)
            print("搜索自动化测试完成")
            time.sleep(0.5)
        elif choice == "exit" or choice == "退出":
            print("程序退出")
            break
        else:
            print("您的输入有误，该功能暂时不可测试。")
