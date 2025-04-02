from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver

def teardown(driver):
    driver.quit()

def check_first_quote():
    driver = setup()
    
    try:
        # Locate the first quote
        first_quote_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//span[@class="text"])[1]'))
        )
        
        actual_text = first_quote_element.text.strip()
        print(actual_text)
        expected_text = ""The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.""
        
        # Use unittest's assertEqual
        assert actual_text == expected_text, "Error Not Equal"
    
    except TimeoutException:
        print("Error: Element not found within the time limit.")
    
    
    teardown(driver)


check_first_quote()



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