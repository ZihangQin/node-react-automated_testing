import time
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException

from src.utils.openHome import open_home

# init_logger()
logger = logging.getLogger("my_logger")


class TestHomeNewQuestion(unittest.TestCase):
    test_data = [
        {"questionTypes": "微积分", "class": "C190603",
         "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。", "difficulty": "易", "score": "10",
         "answer": "8/3", "explains": "全部正确填入"},
        {"questionTypes": "", "class": "C190603", "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。",
         "difficulty": "易", "score": "10", "answer": "8/3", "explains": "试题类型为空"},
        {"questionTypes": "微积分", "class": "", "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。。",
         "difficulty": "易", "score": "10", "answer": "8/3", "explains": "测试班级为空"},
        {"questionTypes": "微积分", "class": "C190603", "title": "", "difficulty": "易", "score": "10", "answer": "8/3",
         "explains": "题目为空"},
        {"questionTypes": "微积分", "class": "C190603",
         "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。", "difficulty": "", "score": "10",
         "answer": "8/3", "explains": "难度为空"},
        {"questionTypes": "微积分", "class": "C190603",
         "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。", "difficulty": "易", "score": "",
         "answer": "8/3", "explains": "分值为空"},
        {"questionTypes": "微积分", "class": "C190603",
         "title": "求该函数 f(x) = x^3 + 2x - 1，在 [-1,1] 区间内的定积分值。", "difficulty": "易", "score": "10",
         "answer": "", "explains": "答案为空"},
        {"questionTypes": "", "class": "",
         "title": "", "difficulty": "", "score": "",
         "answer": "", "explains": "全部不填"},
        {"questionTypes": " ", "class": " ",
         "title": " ", "difficulty": " ", "score": " ",
         "answer": " ", "explains": "全部为空格"}
    ]

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_homeNewQuestion(self):
        open_home(self)
        time.sleep(2)

        # 循环写入新增数据
        for data in self.__class__.test_data:
            # /html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/span
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input_button_add')))
            newTest = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/span")
            newTest.click()
            time.sleep(2)

            logger.info(f"测试路径：http://localhost:3000/index；首页新增试题功能")

            # 获取等价类列表
            questionTypes = data['questionTypes']
            classs = data['class']
            title = data['title']
            difficulty = data['difficulty']
            answer = data['answer']
            score = data['score']
            explains = data['explains']

            # 打印操作日志
            QTNUll = questionTypes
            CLNull = classs
            TINULL = title
            DIFNULL = difficulty
            ANWNULL = answer
            SCORENULL = score
            logger.info(f'测试等价类：{explains}')
            if questionTypes == "":
                QTNUll = "null"
            if classs == "":
                CLNull = "null"
            if title == "":
                TINULL = "null"
            if difficulty == "":
                DIFNULL = "null"
            if answer == "":
                ANWNULL = "null"
            if score == "":
                SCORENULL = "null"
            logger.info(
                f'测试新增试题，试题类型：{QTNUll}；测试班级：{CLNull}；试题题目：{TINULL}；试题难度：{DIFNULL}；试题分值：{SCORENULL}；试题答案：{ANWNULL}')

            # 获取试题类型输入框
            QT = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[1]')
            QT.send_keys(questionTypes)
            time.sleep(2)

            # 获取测试班级输入框
            Class = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[2]')
            Class.send_keys(classs)
            time.sleep(2)

            # 获取题目输入框
            Title = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[3]')
            Title.send_keys(title)
            time.sleep(2)

            # 获取难度输入框
            Difficulty = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[4]')
            Difficulty.send_keys(difficulty)
            time.sleep(2)

            # 获取分值输入框
            Score = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[5]')
            Score.send_keys(score)
            time.sleep(2)

            # 获取试题答案
            Answer = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/input[6]')
            Answer.send_keys(answer)
            time.sleep(2)

            try:
                # 点击确认按钮
                OKSubmit = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
                OKSubmit.click()
                time.sleep(2)
                try:
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text
                    logger.error(f'试题添加失败，失败原因：{alert_text}')

                    alert.accept()
                    time.sleep(2)

                    X = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]')
                    X.click()
                    time.sleep(2)

                    logger.info(
                        "----------------------------------------------------------------------------------------------------------")
                    continue
                except NoAlertPresentException:
                    logger.info(f'试题添加成功')
                    logger.info(
                        "----------------------------------------------------------------------------------------------------------")
                    continue
            except Exception as e:
                print(f'未知错误{e}')

