import time
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def open_home(self):

    url = 'http://localhost:3000/login'
    self.driver.get(url)

    # 输入正确的用户名和密码
    WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'userName')))
    self.driver.find_element(By.ID, 'userName').send_keys('qin')
    time.sleep(1)

    WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'password')))
    self.driver.find_element(By.ID, 'password').send_keys('123456')
    time.sleep(1)

    WebDriverWait(self.driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type=submit]')))
    self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    time.sleep(1)

    WebDriverWait(self.driver, 50).until(EC.alert_is_present())
    time.sleep(1)
    alert = self.driver.switch_to.alert
    alert.accept()
    time.sleep(1)

    # 使用目标 URL 来判断是否跳转到了指定页面
    target_url = 'http://localhost:3000/index'
    WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_url != url)
    assert self.driver.current_url == target_url

    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'Menu')))

    Management = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/ul/li[2]/div/span")
    Management.click()
    time.sleep(1)

    titleManagement = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div[2]/div[1]/ul/li[2]/ul/li[1]/span")
    titleManagement.click()
    time.sleep(1)
