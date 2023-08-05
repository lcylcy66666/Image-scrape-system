import sys
from Services.Scraper import Scraper  
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class InstagramScraperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #Set window size
        self.resize(350, 350)  

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("IG Username")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("IG Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("Keyword")

        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.clicked.connect(self.start_scraping)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Instagram Scraper"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
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
