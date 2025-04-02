from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://quotes.toscrape.com/')
    return driver

def teardown(driver):
    driver.quit()

def check_authorname_block():
    driver = setup()
 
    get_author = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '(//small[@class])')))
    
    while True:
        
        for author_name in get_author:
            assert author_name.is_displayed()
            print('Name is visible')
        
            
                
        try:
            
            next_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
            next_btn.click()
                
        except Exception as e:
                print(e)
                
                
                
    

   
    
  
    teardown(driver)


check_authorname_block()

    
            
            
            
            
           
   
    
 
        
    
        
        
        
        
        
         
        
  
        
    
    
    
    
    