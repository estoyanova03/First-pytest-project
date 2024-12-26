import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email")\
        .send_keys("pytest@email.com")
    driver.find_element(By.ID, "input-password")\
        .send_keys("pytest123")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    print("Log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
    print("Logout")

def test1_order_history_title(setup_teardown):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Order").click()
    assert driver.title == "Order History"
    print("Test 1 Is Complete")


    
    