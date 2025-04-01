from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def setup():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")  
    return driver


def login(driver, username, password):
    user_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="username"]')))
    user_name.send_keys(username)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="password"]')))
    password_field.send_keys(password)
    
    login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@value="Login"]')))
    login_btn.click()

def login_clk(driver):
    log_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'(//p/a)[1]')))
    log_in.click()
    

    
    
   


def assert_successful(driver):
    assert "Quotes to Scrape" in driver.title, "Login failed"
    print("Login successful - Assertion passed!")
    
def assert_validation(driver):
    
    
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//p[@class="error"]')))
    assert error_message.text == "Error while logging in: please, provide your username"
    print(" Invalid login")
    
    

#login with valid username and valid password    
def valid_login(driver):
    
    login_clk(driver)
    login(driver,'admin','admin')
    assert_successful(driver)
    time.sleep(5)
    
    



driver = setup()
valid_login(driver)




driver.quit()