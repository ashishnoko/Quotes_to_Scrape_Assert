
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Test(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://quotes.toscrape.com/")

        
    def test_title(self):
        driver = self.driver
        actual_title = "Quotes to Scrape"
        expected_title =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//h1/a'))).text
        self.assertEqual(actual_title,expected_title,'error')
        
    def test_title(self):
        driver = self.driver
        actual_title = "Quot to Scrape"
        expected_title =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//h1/a'))).text
        self.assertEqual(actual_title,expected_title,'Assertion error')
        
        
    def top10tags(self):
        driver = self.driver
             
        try:
            
            expected_tags = ["love", "inspirational","life","humour","books","reading"]
            top_10_tags = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//span/a[@class="tag"]')))
            
            for tags in top_10_tags:
                assert(tags.is_displayed(), f"tag {tags.text} is not visible")
                
                tag_names = [tags.text for tags in tags]
                
                self.assertIn(tag_names,expected_tags,'f"tag  not found on the page')
                
                
            
                print('Test passed')
                
        except:
            next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Next")]')))
            next_btn.click()
    
    
   
        
    
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

        
        

        
        
    




    
    
    

    
    
