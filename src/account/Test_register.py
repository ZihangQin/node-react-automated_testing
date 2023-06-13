import time
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init_logger()
logger = logging.getLogger("my_logger")


# 该文件用于自动化测试注册功能
class TestRegister(unittest.TestCase):
    test_data = [
        {'username': 'test_1', 'password': '123456', 'phone': '17692111675', 'email': '1420014281@qq.com',
         'explains': '正确的账号密码邮箱手机号'},
        {'username': 'test_1', 'password': '1234567', 'phone': '17692111677', 'email': '1420014282@qq.com',
         'explains': '重复的账号'},
        {'username': 'test_2', 'password': '123456', 'phone': '1', 'email': '1420014281@qq.com',
         'explains': '错误的手机号'},
        {'username': 'test_3', 'password': '123456', 'phone': '17692111675', 'email': '1', 'explains': '错误的邮箱'},
    ]

    def setUp(self):
        # 初始化日志记录器
        self.logger = logger

        # 打开浏览器，进入登录页面
        self.driver = webdriver.Chrome()

    def test_register(self):
        for data in self.__class__.test_data:
            url = "http://localhost:3000/register"

            self.driver.get(url)
            logger.info('测试路径' + url)

            # 绑定注册信息
            explains = data['explains']
            username = data['username']
            phone = data['phone']
            email = data['email']
            password = data['password']

            if phone == '':
                phone = 'null'

            logger.info(f"测试用例：{explains}")
            logger.info(f'测试登录-用户名：{username} 密码：{password} 手机号：{phone} 邮箱：{email}')

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'userName')))
            self.driver.find_element(By.ID, 'userName').send_keys(username)
            time.sleep(2)

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "phone")))
            self.driver.find_element(By.ID, 'phone').send_keys(phone)
            time.sleep(2)

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'email')))
            self.driver.find_element(By.ID, 'email').send_keys(email)
            time.sleep(2)

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'password')))
            self.driver.find_element(By.ID, 'password').send_keys(password)
            time.sleep(2)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type=submit]')))
            self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
            time.sleep(2)

            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text

            if '注册成功' in alert_text:
                logger.info(f"{username}/{password}: 注册成功")
            else:
                logger.error(f"{username}/{password}: 登录失败，提示信息为：{alert_text}")
            alert.accept()
            logger.info("----------------------------------------------------------------------")
