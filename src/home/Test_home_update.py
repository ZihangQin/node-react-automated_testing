import unittest
import logging
import time

from selenium.webdriver import Keys

from src.utils.openHome import open_home
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger("my_logger")


class TestHomeUpdate(unittest.TestCase):
    test_data = [
        {"title": "测试修改功能", "explains": "在任意输入框修改值"},
        {"title": " ", "explains": "在任意输入框输入空格"},
        {"title": "", "explains": "在任意输入框输入不输入内容"},
    ]

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homeUpdate(self):
        open_home(self)
        time.sleep(1)

        logger.info(f"测试路径：http://localhost:3000/index；首页修改试题功能")

        for data in self.__class__.test_data:

            content = data["title"]
            explains = data["explains"]

            logger.info(f"输入内容：{content}；测试用例：{explains}")

            updateTest = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[11]/button')
            updateTest.click()
            time.sleep(2)

            title = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div[2]/div/div/input')
            title.send_keys(Keys.BACKSPACE * 20)
            time.sleep(2)
            title.send_keys(content)
            time.sleep(2)

            OkButton = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
            OkButton.click()

            try:
                # 等待提示框出现，并检查提示信息是否为“登录成功”
                WebDriverWait(self.driver, 3).until(EC.alert_is_present())
                time.sleep(2)
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                if '请正确输入内容' in alert_text:
                    logger.error(f"修改错误：{alert_text}")
                    logger.info(f"----------------------------------------------------------------------------")
                    alert.accept()
                    time.sleep(2)
                else:
                    continue
            except TimeoutException:
                try:
                    WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div')))
                    logger.info(f"修改成功")
                    logger.info(f"----------------------------------------------------------------------------")
                except TimeoutException:
                    print("未知错误")

