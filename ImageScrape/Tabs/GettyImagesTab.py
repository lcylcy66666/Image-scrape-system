from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt
from ..Services.ScrapeGettyimages import  GettyImagesThread

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
        font.setPointSize(18)  
        self.url_input.setFont(font)
        self.keyword_input.setFont(font)
        
        # Initialize getty_scraper attribute
        self.getty_scraper = None  
    
    def start_scraping(self):
        chrome_driver_path = '/Users/lcy/Development/chromedriver'
        getty_url = self.url_input.text()
        keyword = self.keyword_input.text()

        # Create Qt.Thraed instance
        self.getty_thread = GettyImagesThread(chrome_driver_path, getty_url, keyword)

        # connect to slot siginal
        self.getty_thread.finished.connect(self.on_getty_thread_finished)

        # Start Thread
        self.getty_thread.start()

    # After finish then can write some next step here.
    def on_getty_thread_finished(self):
        print("Getty Images scraping thread finished")
        
if __name__ == '__main__':
    app = QApplication([])
    window = GettyImagesTab()
    window.show()
    app.exec_()
