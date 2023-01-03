import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    global driver
    driver_location = '/usr/bin/chromedriver'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=driver_location, options=options)
    driver.implicitly_wait(20)


def test_login(setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "oxd-button").click()
    title = driver.title
    assert title == "OrangeHRM"