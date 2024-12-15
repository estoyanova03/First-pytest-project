from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']")\
    .send_keys("iPhone")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    search_value = driver.find_element(By.XPATH, "//h1[contains(text(),'Search')]").text # selenium method to get the information
    assert "iPhone" in search_value
