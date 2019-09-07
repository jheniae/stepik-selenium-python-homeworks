# -*- coding: utf-8 -*-
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

wd = webdriver.Chrome()
wd.get("http://suninjuly.github.io/explicit_wait2.html")

# Selenium will be checking every 5 seconds, until an element is clickable
price = WebDriverWait(wd, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
wd.find_element_by_id("book").click()

# solution a captcha for robots
value_x = wd.find_element(By.ID, "input_value").text


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


wd.find_element(By.ID, "answer").send_keys(str(calc(value_x)))

submit_button = wd.find_element(By.CSS_SELECTOR, "button[type='submit']")
assert submit_button.get_attribute("disabled") is None
submit_button.click()
