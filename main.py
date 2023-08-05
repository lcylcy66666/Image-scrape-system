import sys
from Services.Scraper import Scraper  
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class InstagramScraperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window size
        self.resize(350, 400)  # Adjusted window height

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setFixedHeight(30)  # Set input box height

        # ADD QLabel for hint
        self.username_label = QLabel("Username:", self)  
        self.username_label.setBuddy(self.username_input)  

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(30)  # Set input box height
                
        # ADD QLabel for hint
        self.password_label = QLabel("Password:", self) 
        self.password_label.setBuddy(self.password_input)  

        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("Keyword")
        self.keyword_input.setFixedHeight(30)  # Set input box height

        # ADD QLabel for hint
        self.keyword_label = QLabel("Keyword:", self)  
        self.keyword_label.setBuddy(self.keyword_input)  

        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.clicked.connect(self.start_scraping)

        layout = QVBoxLayout()
        
        # Add QLabel with larger font and centered alignment
        self.title_label = QLabel("Instagram Scraper", self)
        title_font = QFont("Arial", 40, QFont.Bold)  # Customize font
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.title_label)
        
        # Add QLabel to display guide
        self.guide_label = QLabel(self)
        self.guide_label.setText("1. Enter your Instagram username, password, and search keyword. "
                                 "\n\n2. Then click 'Start Scraping' to begin.")
        self.guide_label.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.guide_label)  # Add the guide label to the layout

        # Set alignment for input widgets and labels
        self.username_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.keyword_input.setAlignment(Qt.AlignCenter)  # Center alignment
        layout.addWidget(self.keyword_label)
        layout.addWidget(self.keyword_input)

        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle("Instagram Scraper System")

    def start_scraping(self):
        username = self.username_input.text()
        password = self.password_input.text()
        keyword = self.keyword_input.text()
        chrome_driver_path = '/Users/lcy/Development/chromedriver'

        scrap = Scraper(chrome_driver_path, username, password, keyword)
        scrap.start_to_scrape()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InstagramScraperApp()
    window.show()
    sys.exit(app.exec_())
