from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time, os, wget

class Scraper:
    def __init__(self, driver_path) -> None:
        ser = Service(driver_path)
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=ser, options=options)
        self.driver.get('https://www.instagram.com/')
        
    def login(self):
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        # HINT: Input your username and password here
        username.send_keys('xxx')
        password.send_keys('xxx')
        login.click()
        
    def search_keyword(self):
        #Open the serch page
        search_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div'))
        )  
        search_button.click()
        
        #Input your keyword
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/ \
                div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
        )
        search_input.send_keys('#corgi')
    
        #Select the keyword you want
        select_the_keyword = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/ \
                div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/ \
                div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div'))
        )
        select_the_keyword.click()
        
    def collect_pic(self):
        start = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/\
                section/main/article/div/div/div/div[1]/div[1]'))
        )
        start.click()
        
        # Click to the next pic
        next_pic_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/\
                div/div/div/div/div[1]/div/div/div/button'))
        )
        next_pic_button.click()
        
        
    def start_to_scrape(self):
        self.login()
        self.search_keyword()
        self.collect_pic()
        
        # self.driver.quit()
        
        
if __name__ == '__main__':
    chrome_driver_path = '/Users/lcy/Development/chromedriver'
    scrap = Scraper(chrome_driver_path)
    scrap.start_to_scrape()