from ..Services.ScrapeGettyimages import GettyImagesScraper
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QTabWidget,QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GettyImagesTab(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Getty Images Scraper")
        self.resize(400, 300)
        
        layout = QVBoxLayout()

        url_layout = QHBoxLayout()  # Create a horizontal layout for URL input
        url_label = QLabel("URL:")  # Create a QLabel for the label "URL"
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Getty Images URL")
        self.url_input.setText("https://www.gettyimages.hk/")  # Set default URL
        self.url_input.setMinimumHeight(40)  # Set the minimum height
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        
        keyword_layout = QHBoxLayout()  # Create a horizontal layout for keyword input
        keyword_label = QLabel("Keyword:")
        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("Enter a keyword")
        self.keyword_input.setMinimumHeight(40)
        keyword_layout.addWidget(keyword_label)
        keyword_layout.addWidget(self.keyword_input)
        
        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.clicked.connect(self.start_scraping)
        layout.addLayout(url_layout)  # Add the URL layout to the main layout
        layout.addLayout(keyword_layout)  # Add the keyword layout to the main layout
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        
        # Set font for the input fields
        font = QFont()
        font.setPointSize(14)  # Set the font size
        self.url_input.setFont(font)
        self.keyword_input.setFont(font)
    
    def start_scraping(self):
        chrome_driver_path = '/Users/lcy/Development/chromedriver'
        getty_url = self.url_input.text()
        keyword = self.keyword_input.text()

        # Add your Getty Images scraping logic here
        getty_scraper = GettyImagesScraper(chrome_driver_path, getty_url, keyword)
        getty_scraper.start_scraping_getty_images()
        print("Scraping Getty Images:", getty_url, "with keyword:", keyword)