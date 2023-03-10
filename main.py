import random
import time

import requests
from faker import Faker
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
import subprocess
import utilities as utils

fake = Faker()
config = utils.read_config()
options = Options()
THR_url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.61512805.853185086.1677227212-2135743068.1677227211'
options.add_argument("--headless")

headers = {
    'User-Agent': fake.user_agent(),
    'Accept-Language': 'en-US,en;q=0.5'
}

# 启动 secret-agent 代理
subprocess.Popen(['secret-agent', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 创建 secret-agent 代理
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = 'http://127.0.0.1:9191'
proxy.ssl_proxy = 'http://127.0.0.1:9191'

# 创建 selenium WebDriver，并使用 secret-agent 代理
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy.http_proxy)
driver = webdriver.Chrome(options=options)


response = requests.get(THR_url, headers=headers)
print(response.text)

start_station = config.get('start_station')
end_station = config.get('end_station')
start_time = config.get('start_time')
regular_ticket = int(config.get('regular_ticket'))
children_ticket = int(config.get('children_ticket'))
disabled_ticket = int(config.get('disabled_ticket'))
student_ticket = int(config.get('student_ticket'))
senior_persons_ticket = int(config.get('senior_persons_ticket'))
early_ticket = config.get('early')


def driver_send_keys_xpath(locator, key):
    """Send keys to element.
    :param locator: Locator of element.
    :param key: Keys to send.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(key)


def driver_click_xpath(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))).click()


def driver_screenshot(locator, path):
    """Take screenshot of element.
    :param locator: Locator of element.
    :param path: Path to save screenshot.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(locator)).screenshot(path)


def driver_click(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(locator)).click()


def enter():
    driver.get(THR_url)
    driver.maximize_window()
    try:
        driver_click_xpath("//*[@id='cookieAccpetBtn']")
    except TimeoutException:
        pass
    print("進入系統")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select/option[{start_station}]')
    print("已輸入起站")
    time.sleep(random.uniform(1, 3))
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select/option[{end_station}]')
    print("已輸入迄站")
    time.sleep(random.uniform(1, 3))
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[1]/select/option[{start_time}]')
    print("已輸入出發時間")
    time.sleep(random.uniform(1, 3))
    driver_click_xpath("//*[@id='BookingS1Form']/div[3]/div[2]/div/div[1]/div[1]/input[2]")
    driver_click_xpath("//*[@id='mainBody']/div[9]/div[2]/div/div[2]/div[2]/span[21]")
    print("已輸入日期")
    time.sleep(random.uniform(1, 3))
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[4]/div[1]/div[1]/div/select/option[{regular_ticket + 1}]')
    print("已輸入全票")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[4]/div[1]/div[2]/div/select/option[{children_ticket + 1}]')
    print("已輸入孩童票")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[4]/div[1]/div[3]/div/select/option[{disabled_ticket + 1}]')
    print("已輸入愛心票")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[4]/div[1]/div[4]/div/select/option[{student_ticket + 1}]')
    print("已輸入大學生票")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[4]/div[1]/div[5]/div/select/option[{senior_persons_ticket + 1}]')
    print("已輸入敬老票")
    driver_screenshot((By.XPATH, "//*[@id='BookingS1Form_homeCaptcha_passCode']"), "captcha.png")
    driver_send_keys_xpath("//*[@id='securityCode']", utils.get_ocr_password("captcha.png"))
    time.sleep(random.uniform(1, 3))
    if early_ticket == 1:
        driver_click_xpath('//*[@id="onlyQueryOffPeakCheckBox"]')
    driver_click_xpath('//*[@id="SubmitButton"]')
    time.sleep(10000)


if __name__ == '__main__':
    enter()
    driver.quit()
    subprocess.Popen(['secret-agent', 'stop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)