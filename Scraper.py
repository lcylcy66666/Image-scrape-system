from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time, os, requests

class Scraper:
    def __init__(self, driver_path, username, password, keyword) -> None:
        self.username = username
        self.password = password
        self.keyword = keyword
        self.driver = self.setup_driver(driver_path)
    
    def setup_driver(self, driver_path):
        ser = Service(driver_path)
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser, options=options)
        driver.get('https://www.instagram.com/')
        return driver
    
    def login(self):
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        username.send_keys(self.username)
        password.send_keys(self.password)
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
        search_input.send_keys(self.keyword)
    
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

        time.sleep(2)
        
        for count in range(5):
            #Download pictures
            div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '._aagv img'))
            )
            self.download_pic(div, count)

            time.sleep(2)

            # Click to the next pic
            next_pic_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/\
                    div/div/div/div/div[1]/div/div/div/button'))
            )
            next_pic_button.click()
            
    def download_pic(self, div, count):
        print(div)
        scrape_image = div.get_attribute('src')
        
        tag_folder = os.path.join(self.keyword)

        if not os.path.exists(tag_folder):
            os.mkdir(tag_folder)
            print(f"Folder '{self.keyword}' created at {tag_folder}")
        else:
            print(f"Folder '{self.keyword}' already exists at {tag_folder}")
        
        save_as = os.path.join(tag_folder, self.keyword+str(count) + '.jpg')
        
        
        #使用requests下載，wget還在測試
        response = requests.get(scrape_image)
        
        if response.status_code == 200:
            with open(save_as, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {save_as}")
        else:
            print("Failed to download image")   
            
        print('Start to download!')
         
        
    def start_to_scrape(self):
        self.login()
        self.search_keyword()
        self.collect_pic()        
        
        time.sleep(5)
        self.driver.quit()
        
        
if __name__ == '__main__':
    chrome_driver_path = '/Users/lcy/Development/chromedriver'
    
    # HINT: Input your username and password here
    username= 'xxx'
    password='xxx'
    
    # HINT: You can change to your keyword
    keyword ='#corgi'
    scrap = Scraper(chrome_driver_path, username, password)
    scrap.start_to_scrape()