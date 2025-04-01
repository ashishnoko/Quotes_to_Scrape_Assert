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
    
def index():
    driver = setup()
    
 
   
    
    a = 1 
    while (a < 11):
        
        footer_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'(//p/a[@href])[2]')))
        next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Next")]')))
        next_btn.click()
     
        
        
        
        try:
            assert footer_link.text == "GoodReads.com"
            print('test passed')
            time.sleep(3)
        except Exception as e :
            print(f'test failed : {e}')
            
        a = a + 1
            
            
            
    
        
        
    
    
    teardown(driver)
    
index()