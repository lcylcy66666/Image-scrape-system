from Services.Scraper import Scraper
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QTabWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class InstagramTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.title_label = QLabel("Instagram Scraper", self)
        title_font = QFont("Arial", 40, QFont.Bold)  # Customize font
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.title_label)

        self.guide_label = QLabel(self)
        self.guide_label.setText("1. Enter the URL of the web page you want to scrape, "
                                 "Instagram username, password, and search keyword. "
                                 "\n\n2. Then click 'Start Scraping' to begin.")
        self.guide_label.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.guide_label)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Web page URL you want to scrape")
        self.url_input.setFixedHeight(35)
        self.url_label = QLabel("The URL you want to scrape:", self)  
        self.url_label.setBuddy(self.url_input)  
        self.url_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.url_label)  # Add URL input
        layout.addWidget(self.url_input)  # Add URL input

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedHeight(35)
        self.username_label = QLabel("Username:", self)  
        self.username_label.setBuddy(self.username_input)  
        self.username_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.username_label)  
        layout.addWidget(self.username_input)  

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(35)
        self.password_label = QLabel("Password:", self)  
        self.password_label.setBuddy(self.password_input)  
        self.password_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.password_label)  
        layout.addWidget(self.password_input)  

        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("Keyword")
        self.keyword_input.setFixedHeight(35)
        self.keyword_label = QLabel("Keyword:", self)  
        self.keyword_label.setBuddy(self.keyword_input)  
        self.keyword_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.keyword_label)  
        layout.addWidget(self.keyword_input)  

        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.setFixedHeight(50)  # Set button height
        self.start_button.setStyleSheet("font-size: 16px; width: 25%; margin: 0 auto;")  # Adjust style
        self.start_button.clicked.connect(self.start_scraping)
        layout.addWidget(self.start_button)  # Add start button

        self.setLayout(layout)

    def start_scraping(self):
        url = self.url_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        keyword = self.keyword_input.text()
        chrome_driver_path = '/Users/lcy/Development/chromedriver'

        scrap = Scraper(chrome_driver_path, url, username, password, keyword)
        scrap.start_to_scrape()
