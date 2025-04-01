from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time





def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver
    

def teardown(driver):
    driver.quit()


def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver
    

def teardown(driver):
    driver.quit()
    
def index():
    driver = setup()
    
    
    #wait for the title to appear
    a = 1
    while (a < 10):
    
        quote_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'(//span[@class="text"])[1]')))
        next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Next")]')))
        next_btn.click()
        
        expected_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//h1/a')))
        
        try: 
            
            assert expected_title.text == "Quotes to Scrape"
            print('Test passed')
        
        except Exception as e:
            print(f'Error as {e}')
        
        a = a + 1
    
    
    teardown(driver)
    
    
    
    
index()
