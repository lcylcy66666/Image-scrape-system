from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PyQt5.QtCore import QThread, pyqtSignal

import time, os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)
from ImageScrape.Services.Scraper import Scraper


class GettyImagesScraper(Scraper, QThread):
    src_list_received = pyqtSignal(list)  # Define a new signal
    dowload_progress = pyqtSignal(int)
    dowload_finish = pyqtSignal(bool)
    progress_hint = pyqtSignal(str)
    
    # Define a signal for progress display    
    def __init__(self, driver_path, URL, keyword):
        super().__init__(driver_path, URL, keyword, "", "")  
        QThread.__init__(self)  # Call QThread's constructor

        self.src_list = []

    def run(self):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="phrase"]'))
            )
            search_input.send_keys(self.keyword)
            
            search_click = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.fpCrYgH1yrrw1HEKyQRN'))
            )
            search_click.click()
            
            # Cause getty images will prevent BOT so sometimes can't access data
            
            try:
                total_pages_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'JO4Dw2C5EjCB3iovKUcw'))
                )
                total_pages = total_pages_element.text
            except TimeoutException:
                print("Total pages element not found within 10 seconds.")
                self.driver.quit()  

            
            for page in range(int(total_pages)):
                print('Loading Page: ', page)
                self.progress_hint.emit(f"Loading page: {page}")
                
                if page < int(total_pages) - 1:
                    try:
                        next_button = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="pagination-button-next"]'))
                        )
                        
                        # Why 60 cause each page only show 60 pictures
                        imgs = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/section/div/main/div/div/div[4]/div[2]/div[2]'))
                        )

                        img_tags = imgs.find_elements(By.CLASS_NAME, 'BLA_wBUJrga_SkfJ8won')

                        # Add img_src to list
                        for img_tag in img_tags:
                            src = img_tag.get_attribute('src')
                            self.src_list.append(src)
                        
                        next_button.click()
                        time.sleep(2)
                        
                    except TimeoutException:
                        print("Last page reached. Exiting loop.")
                        break
                else:
                    print("Last page reached. Exiting loop.")
                    break
                
            # Finish scraping and close driver
            self.driver.quit()
            
            # Emit the src_list_received signal
            self.src_list_received.emit(self.src_list)
            
        except Exception as e:
            print('Error in scraping getty-images: ', e)
            return
            
        print('Total Images: ', len(self.src_list))
        
        # Download the pictures
        for i in range(len(self.src_list)):
            self.dowload_progress.emit(i)
            self.download_pic(self.src_list[i], i)
        # Download successfully signale emit
        self.dowload_finish.emit(True)  
        # print("Scraping Getty Images:", self.URL)
        # print('Now bot are scraping for', self.keyword)

if __name__ == '__main__':
    chrome_driver_path = '/Users/lcy/Development/chromedriver'
    getty_url = "https://www.gettyimages.hk/"
    keyword = "corgi"
    
    getty_scraper = GettyImagesScraper(chrome_driver_path, getty_url, keyword)
    getty_scraper.run()
