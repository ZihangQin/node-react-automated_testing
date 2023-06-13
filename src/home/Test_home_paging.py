import json
import unittest
import logging
import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.utils.openHome import open_home

logger = logging.getLogger("my_logger")


class TestHomePaging(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homePaging(self):
        open_home(self)
        time.sleep(2)

        logger.info(f"测试路径：http://localhost:3000/index；首页分页功能")

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
        }

        # 定义请求参数（请更改为实际的请求参数）
        params = {
            'page': '2',
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMiIsInVzZXJuYW1lIjoicWluIiwiZXhwIjoxNjg2NzM4Nzk0LCJpYXQiOjE2ODY2NTIzOTR9.FgnQi3sAR5uxVt270q_hQSrB-9FAYJJhgKQoAReS_JE',
        }

        # 发送GET请求
        response = requests.get("http://127.0.0.1:8080/api/browse/testList", headers=headers, params=params)

        # 输出响应结果
        response_json = json.loads(response.text)
        pages = response_json["Data"]["TitlePages"]
        if pages <= 1 and response.status_code == 200:
            if "token验证失败" in response_json["Msg"]:
                logger.error(f"token验证失败，请更换paging测试脚本请求中的token值")
                logger.info(f"-----------------------------------------")
                return
            print(pages)
            logger.error(f"当前数据页数为：{pages}；当前无法分页")
            logger.info(f"-----------------------------------------")
            return

        logger.info(f"测试路径：http://localhost:3000/index；主页分页功能")
        logger.info(f"点击数字进行分页请求")

        OnClickPaging = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[3]/ul/li[3]/a')
        OnClickPaging.click()
        time.sleep(2)

        logger.info(f"点击数字进行分页请求成功")
        logger.info("---------------------------------------------")

        logger.info(f"点击箭头进行分页请求")

        OnClickArrows = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[3]/ul/li[6]/button')
        OnClickArrows.click()
        time.sleep(2)

        logger.info(f"点击箭头分页请求成功")
        logger.info("---------------------------------------------")
