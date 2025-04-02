from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver

def teardown(driver):
    driver.quit()

def check_authorname_block():
    driver = setup()

    try:
        while True:
          
            authors = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))

            for author in authors:
                assert author.is_displayed()
                print(f'Author: {author.text} is visible')

            
            try:
                next_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
                next_btn.click()
                
            except Exception as e:
                print("No more pages")
                break

    except Exception as e:
        print(f"Error: {e}")

    
    teardown(driver)

check_authorname_block()

