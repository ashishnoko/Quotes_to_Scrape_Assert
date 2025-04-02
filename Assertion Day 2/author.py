from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest
import time

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://quotes.toscrape.com/')

    def tearDown(self):
        self.driver.quit()
        
        
    def test_first_author(self):
       
        try:
            
            author_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//small[@class="author"])[1]')))
            print(author_element.text)
            self.assertTrue(author_element.is_displayed(),'Error')
        except Exception as e:
            print(e)
            
            
    def test_next_button(self):
       
        try:
            next_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li/a")))
            time.sleep(4)

            self.assertTrue(next_button.is_displayed(), "Next button is not displayed.")

        except Exception as e:
            print(e)


            

    def test_firstpage(self):
      
        try:
           
            get_all_author = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))

        
                
            author_numbers = len(get_all_author)
                
            print(f"Number of author in first page: {author_numbers}")
                
            self.assertGreater(author_numbers,5," There are less number of author in this page")
           
           

        except Exception as e :
            print(e)
            
    def test_second_page(self):
        
        next_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//small[@class]'))).click()
        time.sleep(5)
        try:
           
            get_all_author = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))

        
                
            author_numbers = len(get_all_author)
                
            print(f"Number of author in second page: {author_numbers}")
                
            self.assertGreater(author_numbers,5," There are less number of author in this page")
           
           

        except Exception as e :
            print(e)



if __name__ == "__main__":
    unittest.main()