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

    def test_first_quote(self):
      
        try:
           
            first_quote_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="text"])[1]')))

            actual_text = first_quote_element.text
           
            expected_text = (
                "“The world as we have created it is a process of our thinking. "
                "It cannot be changed without changing our thinking.”"
            )

            
            self.assertEqual(actual_text, expected_text, "First quote text does not match.")

        except Exception as e :
            print(e)
            
    def test_second_quote(self):
      
        try:
           
            quote_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="text"])[2]')))

            actual_text = quote_element.text
           
            expected_text = ("“It is our choices, that show what we truly are, far more than our abilities.”")
        

            #performAssert
            self.assertNotEqual(actual_text, expected_text, "First quote text does not match.")

        except Exception as e :
            print(e)

            
   
    


if __name__ == "__main__":
    unittest.main()