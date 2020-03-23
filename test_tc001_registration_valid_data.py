from selenium.webdriver import Chrome
from selenium import webdriver 
from TestCases.Base import initiate_driver


def test_validate_registration():
    driver= initiate_driver.startBrowser()
    driver.find_element_by_name('fld_username').send_keys('Tania')