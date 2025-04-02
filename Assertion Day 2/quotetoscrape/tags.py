from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://quotes.toscrape.com/')

    def tearDown(self):
        self.driver.quit()
        
    
    #test top 10 tags

    def test_top_tags(self):
      
        try:
           
            tags_element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class]/a[@class]')))
            for tags in tags_element:
                
                expected_tags = ["love", "inspirational","life","humor","books","reading","friendsip","friends","truth","simile"]
                
              

                
                self.assertIn("noko", expected_tags, "Expected 'Love' in the list of tags but it's missing.")
                
           
                
                     
            


        except Exception as e :
            print(e)
            
    def test_top_tags(self):
       
      
        try:
            
          
            title_tags = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h2')))

            self.assertTrue(title_tags.is_displayed(), "Top 10 tags is not displayed.")
           
            
           
       
                
                
        except Exception as e :
            print(e)        
            
    
    


if __name__ == "__main__":
    unittest.main()