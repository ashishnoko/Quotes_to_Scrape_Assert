import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAuthorName(unittest.TestCase):

    def setUp(self):
   
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://quotes.toscrape.com/')
    
    def tearDown(self):
      
        self.driver.quit()
    
    def test_author_name_visibility(self):
       
        try:
          
            authors = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))
            
         
            for author in authors:
                self.assertTrue(author.is_displayed(), f"Author {author.text} is not visible")
                print(f'Author: {author.text} is visible')
        
        except TimeoutException:
            self.fail("Authors not found on the page.")
    
    def test_author_name(self):
        
        expected_authors = ["Albert Einstein", "J.K. Rowling", "Marilyn Monroe"]  
        
        try:
            authors = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))
            
     
           
            author_names = [author.text for author in authors]
            
            for author in expected_authors:
                self.assertIn(author, author_names, f"Author {author} not found on the page")
        
        except TimeoutException:
            self.fail("Authors not found on the page.")
            
    
            
    
            
            
        

if __name__ == "__main__":
    unittest.main()
