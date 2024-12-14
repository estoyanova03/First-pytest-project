from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title: ", driver.title)

def test2_lambdatest_ecommerce():
    dirver = webdriver.Chrome()
    dirver.maximize_window()
    dirver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title: ", dirver.title)

def testRexWebsite():
    dirver = webdriver.Chrome()
    dirver.maximize_window()
    dirver.get("https://rexjones2.com/")
    print("Title: ", dirver.title)

def google_test():
    dirver = webdriver.Chrome()
    dirver.maximize_window()
    dirver.get("https://google.com/")
    print("Title: ", dirver.title)