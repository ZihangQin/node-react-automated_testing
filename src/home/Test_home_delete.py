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


class TestHomeDelete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homeDelete(self):
        open_home(self)
        time.sleep(1)

        logger.info(f"测试路径：http://localhost:3000/index；首页删除功能")

        deleteButton = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[11]/a")
        deleteButton.click()
        time.sleep(2)

        notDelete = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/button[1]/span')
        notDelete.click()
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div')))
            print("取消删除成功")
            time.sleep(2)

            deleteButton.click()
            time.sleep(2)
            onDelete = self.driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[2]/div/div/div/div[2]/button[2]/span')
            onDelete.click()
            time.sleep(2)

            try:
                WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div')))
                logger.info(f"删除成功")
                logger.info(f"--------------------------------------------------")
            except TimeoutException:
                logger.error(f"未获取到删除成功的提示信息")
        except TimeoutException:
            logger.error(f"未获取到取消删除成功的提示信息")
