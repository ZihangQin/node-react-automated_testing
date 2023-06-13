import time
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# init_logger()
logger = logging.getLogger("my_logger")


# 该文件用于自动化测试登录功能
class TestLogin(unittest.TestCase):
    test_data = [
        {'username': 'test_1', 'password': '123456', 'explains': '正确的账号密码'},
        {'username': 'test_user', 'password': '123456', 'explains': '错误的账号正确的密码'},
        {'username': 'qin', 'password': '123456789', 'explains': '正确的账号错误的密码'}
    ]

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        for data in self.__class__.test_data:
            url = 'http://localhost:3000/login'
            explains = data['explains']
            username = data['username']
            password = data['password']

            self.driver.get(url)
            logger.info(f"测试路径：{url}")
            logger.info(f"测试用例：{explains}")
            logger.info(f'测试登录-用户名：{username}和密码：{password}')

            # 输入正确的用户名和密码
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'userName')))
            self.driver.find_element(By.ID, 'userName').send_keys(username)
            time.sleep(2)

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'password')))
            self.driver.find_element(By.ID, 'password').send_keys(password)
            time.sleep(2)

            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type=submit]')))
            self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
            time.sleep(2)

            # 等待提示框出现，并检查提示信息是否为“登录成功”
            WebDriverWait(self.driver, 50).until(EC.alert_is_present())
            time.sleep(2)
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if '登录成功' in alert_text:
                logger.info(f"{username}/{password}: 登录成功")
            else:
                logger.error(f"{username}/{password}: 登录失败，提示信息为：{alert_text}")
            alert.accept()
            logger.info("----------------------------------------------------------------------")
            # self.driver.quit()
