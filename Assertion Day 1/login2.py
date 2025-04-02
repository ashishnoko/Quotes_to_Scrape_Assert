import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")
    driver.maximize_window()
    return driver


def test_first_quote():
    driver = create_driver()
    wait = WebDriverWait(driver, 15)
    try:
        quoteElem = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='text'])[1]"))
        )
        actualResult = quoteElem.text
        expectedResult = "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"

        print(f"Actual Result: {actualResult}")
        print(f"Expected Result: {expectedResult}")

        unittest.TestCase().assertEqual(actualResult, expectedResult, "First quote does not match!")
        print("Success: First quote verification passed!")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    driver.quit()
    
test_first_quote()

