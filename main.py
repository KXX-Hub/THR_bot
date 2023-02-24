import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import utilities as utils

config = utils.read_config()
chrome = webdriver.Chrome()

options = Options()
options.add_argument("--disable-notifications")

tw_hs_url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.61512805.853185086.1677227212-2135743068.1677227211'
start_station = config.get('start_station')
end_station = config.get('end_station')


def chrome_send_keys(locator, key):
    """Send keys to element.
    :param locator: Locator of element.
    :param key: Keys to send.
    """
    WebDriverWait(chrome, 10).until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(key)


def chrome_click(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(chrome, 10).until(ec.presence_of_element_located((By.XPATH, locator))).click()


def enter():
    chrome.get(tw_hs_url)
    try:
        chrome_click("//*[@id='cookieAccpetBtn']")
    except TimeoutException:
        pass
    print("進入系統")
    chrome_click(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select/option[{start_station+1}]')
    print("以輸入起站:")
    chrome_click(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select/option[{end_station+1}]')
    print("以輸入迄站:")
    time.sleep(1000)


if __name__ == '__main__':
    enter()
    chrome.quit()
