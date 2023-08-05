from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time, os, requests

class Scraper:
    def __init__(self, driver_path, URL, username, password, keyword) -> None:
        self.URL = URL
        self.username = username
        self.password = password
        self.keyword = keyword
        self.driver_path = driver_path  # 初始化 self.driver_path
        self.driver = self.setup_driver()
    
    def setup_driver(self):
        ser = Service(self.driver_path)
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser, options=options)
        driver.get(self.URL)
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
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]'))
        )
        start.click()
        
        time.sleep(2)
        
        # self.driver.refresh()

        for count in range(5):
            # Candidate pictures
            div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '._aagv img'))
            )
            scrape_image = div.get_attribute('src')
            print('ING_URL: ', scrape_image)

            # self.download_pic(scrape_image, count)

            time.sleep(2)

            
            # Click to the next pic
            next_button_xpath = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button'
            if count > 0:
                next_button_xpath = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button'
            
            next_pic_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, next_button_xpath))
            )
            next_pic_button.click()
            
            time.sleep(2)


    def download_pic(self, scrape_image, count):
        tag_folder = os.path.join(self.keyword)

        if not os.path.exists(tag_folder):
            os.mkdir(tag_folder)
            print(f"Folder '{self.keyword}' created at {tag_folder}")
        else:
            pass
        
        save_as = os.path.join(tag_folder, self.keyword+str(count) + '.jpg')
        
        
        #Use requests to download
        response = requests.get(scrape_image)
        
        if response.status_code == 200:
            with open(save_as, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {save_as}")
        else:
            print("Failed to download image")   
            
        # print('Start to download!')
         
        
    def start_to_scrape(self):
        self.login()
        self.search_keyword()
        self.collect_pic()        
        
        time.sleep(5)
        self.driver.quit()
        
        
if __name__ == '__main__':
    # HINT: Change to your own chromedriver path
    chrome_driver_path = '/Users/lcy/Development/chromedriver'
    
    # HINT: Input your username and password and URL here
    search_URL = 'https://www.instagram.com/'
    username= 'xxx'
    password='xxx'
    
    # HINT: You can change to your keyword
    keyword ='#corgi'
    scrap = Scraper(chrome_driver_path, search_URL, username, password, keyword)
    scrap.start_to_scrape()