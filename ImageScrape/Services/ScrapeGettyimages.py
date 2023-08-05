from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time, os, requests, sys

current_dir = os.path.dirname(os.path.abspath(__file__))

root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from ImageScrape.Services.Scraper import Scraper


class GettyImagesScraper(Scraper):
    def __init__(self, driver_path, URL, keyword) -> None:
        # 只傳遞需要的參數
        super().__init__(driver_path, URL, "", "", keyword)  
        self.driver = self.setup_driver(driver_path)

    def start_scraping_getty_images(self):
        print("Scraping Getty Images:", self.URL)
    
    

if __name__ == '__main__':
    chrome_driver_path = '/Users/lcy/Development/chromedriver'
    getty_url = "https://www.gettyimages.hk/"
    keyword = "corgi"
    
    getty_scraper = GettyImagesScraper(chrome_driver_path, getty_url, keyword)
    getty_scraper.start_scraping_getty_images()