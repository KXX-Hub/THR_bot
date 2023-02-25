import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import utilities as utils

config = utils.read_config()
driver = webdriver.Chrome()

options = Options()
options.add_argument("--disable-notifications")

tw_hs_url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.61512805.853185086.1677227212-2135743068.1677227211'
start_station = config.get('start_station')
end_station = config.get('end_station')
start_time = config.get('start_timed')


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


def driver_click(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(locator)).click()


def enter():
    driver.get(tw_hs_url)
    try:
        driver_click_xpath("//*[@id='cookieAccpetBtn']")
    except TimeoutException:
        pass
    print("進入系統")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select/option[{start_station + 1}]')
    print("已輸入起站")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select/option[{end_station + 1}]')
    print("已輸入迄站")
    #    driver_click_xpath("//*[@id='mainBody']/div[9]/div[2]/div/div[2]/div[1]/span[29]")
    #    print("已輸入日期")
    #    driver_click_xpath("//*[@id='BookingS1Form']/div[3]/div[2]/div/div[2]/div[1]/select/option[2]")
    driver_click_xpath(f'//*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[1]/select/option[{start_time}]')
    print("已輸入出發時間")
    time.sleep(1000)


if __name__ == '__main__':
    print(config.get('start_time'))
    enter()
    driver.quit()
# //*[@id="BookingS1Form"]/div[3]/div[2]/div/div[2]/div[1]/select/option[2]
