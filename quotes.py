from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver

def teardown(driver):
    driver.quit()

def check_total_quotes():
    driver = setup()
    total_quotes = 0

    while True:
       
        quotes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="text"]'))
        )
        total_quotes = total_quotes + len(quotes)

        try:
           
            next_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
            next_btn.click()
        except Exception as e:
            print(e)
            break

    print(f"Total number of quotes: {total_quotes}")
    
    expected_quotes = 100
    
    assert total_quotes == expected_quotes,'Test failed'
    print('Test passed')
    teardown(driver)


check_total_quotes()
