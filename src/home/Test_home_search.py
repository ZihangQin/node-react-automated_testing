import unittest
import logging
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.utils.openHome import open_home

logger = logging.getLogger("my_logger")


class TestHomeSearch(unittest.TestCase):
    test_data = [
        {"search_value": "定积分", "explains": "能搜索到内容的"},
        {"search_value": "kkkkkkkkkkk", "explains": "搜索无内容"}
    ]

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homeSearch(self):
        open_home(self)
        time.sleep(2)

        for data in self.__class__.test_data:
            search_value = data['search_value']
            explains = data['explains']

            logger.info(f"测试路径：http://localhost:3000/index；首页搜索功能")
            logger.info(f"搜索框输入值：{search_value}，测试用例：{explains}")

            # 获取搜索框
            searchInput = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/input[1]')
            searchInput.send_keys(search_value)
            time.sleep(2)

            # 获取搜索按钮
            searchButton = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/input[2]')
            searchButton.click()
            time.sleep(3)

            try:
                # 等待弹窗出现
                WebDriverWait(self.driver, 3).until(EC.alert_is_present())

                # 获取弹窗并进行相应操作
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print(alert_text)
                alert.accept()
                logger.error(f"{alert_text}")
                logger.info(f"搜索完成，无结果")
                logger.info(f"-------------------------------------------------------")
            except TimeoutException:
                logger.info(f"搜索成功，有结果")
                logger.info(f"-------------------------------------------------------")

