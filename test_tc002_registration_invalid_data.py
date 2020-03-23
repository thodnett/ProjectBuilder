
from TestCases.Base import initiate_driver

def test_registration_invalid_data():
    driver=initiate_driver.startBrowser()
    driver.find_element_by_name('phone').send_keys('12345')