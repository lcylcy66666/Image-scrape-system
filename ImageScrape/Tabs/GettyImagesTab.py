from ..Services.ScrapeGettyimages import GettyImagesScraper
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QTabWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GettyImagesTab(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Getty Images Scraper")
        self.resize(400, 300)
        
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Getty Images URL")
        self.url_input.setText("https://www.gettyimages.hk/")  # Set default URL
        layout.addWidget(self.url_input)
        
        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.clicked.connect(self.start_scraping)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
    
    def start_scraping(self):
        chrome_driver_path = '/Users/lcy/Development/chromedriver'
        getty_url = self.url_input.text()
        getty_url = self.url_input.text()
        keyword = self.keyword_input.text()

        # Add your Getty Images scraping logic here
        getty_scraper = GettyImagesScraper(chrome_driver_path, getty_url, keyword)
        getty_scraper.start_scraping_getty_images()
        print("Scraping Getty Images:", getty_url)