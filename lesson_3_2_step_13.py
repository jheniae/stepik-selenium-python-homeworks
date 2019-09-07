# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestWelcome(unittest.TestCase):
    wd = None

    def setUp(self):
        self.wd = webdriver.Chrome()

    def tearDown(self):
        self.wd.close()

    def test_for_registration1(self):
        wd = self.wd
        link = "http://suninjuly.github.io/registration1.html"
        wd.get(link)

        # fill required fields
        input_name = wd.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.first")
        input_name.send_keys("Name")

        input_second_name = wd.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.second")
        input_second_name.send_keys("Second Name")

        input_email = wd.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.third")
        input_email.send_keys("Email")

        # send filed form
        button = wd.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # check that registration is successful
        # wait until page is loaded
        elt = WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text_elt = wd.find_element(By.TAG_NAME, "h1")
        welcome_text_elt = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text_elt)

    def test_for_registration2(self):
        wd = self.wd
        link = "http://suninjuly.github.io/registration2.html"
        wd.get(link)

        # fill required fields
        input_name = wd.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.first")
        input_name.send_keys("Name")

        input_email = wd.find_element(
            By.CSS_SELECTOR, ".first_block .form-control.third")
        input_email.send_keys("Email")

        # send filed form
        button = wd.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # check that registration is successful
        # wait until page is loaded
        elt = WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text_elt = wd.find_element(By.TAG_NAME, "h1")
        welcome_text_elt = welcome_text_elt.text

        self.assertEqual(
            "You have successfully registered!",
            welcome_text_elt)


if __name__ == "__main__":
    unittest.main()
