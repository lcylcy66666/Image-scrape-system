from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar,QTextEdit
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtCore import pyqtSignal, Qt
from ..Services.ScrapeGettyimages import  GettyImagesThread

class GettyImagesTab(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Getty Images Scraper")
        self.resize(400, 300)
        
        layout = QVBoxLayout()

        # Create URL input layout
        url_layout = QHBoxLayout()
        url_label = QLabel("URL:")
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Getty Images URL")
        self.url_input.setText("https://www.gettyimages.hk/")  # Set default URL
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)

        # Create keyword input layout
        keyword_layout = QHBoxLayout()
        keyword_label = QLabel("Keyword:")
        self.keyword_input = QLineEdit(self)
        self.keyword_input.setPlaceholderText("Enter a keyword")
        keyword_layout.addWidget(keyword_label)
        keyword_layout.addWidget(self.keyword_input)
        
        # Create start button layout
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Scraping", self)
        self.start_button.clicked.connect(self.start_scraping)
        self.start_button.setStyleSheet("font-size: 16px;")
        self.start_button.setMaximumWidth(150)  
        # button_layout.addStretch(1) 
        button_layout.addWidget(self.start_button)
        
        # Create progress bar layout
        self.progress_bar = QProgressBar(self)

        self.log_text_edit = QTextEdit(self)
        self.log_text_edit.setReadOnly(True)  # 设置为只读

        # Add layouts to main layout
        layout.addLayout(url_layout)
        layout.addLayout(keyword_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.log_text_edit)

        # Set font for the input fields
        font = QFont()
        font.setPointSize(18)  
        self.url_input.setFont(font)
        self.keyword_input.setFont(font)
        
        # Initialize getty_scraper attribute
        self.getty_scraper = None  
    
        self.setLayout(layout)
        
    # Override the keyPressEvent method
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_W and (event.modifiers() & Qt.ControlModifier or event.modifiers() & Qt.MetaModifier):
            # Quit the whole application
            QApplication.quit() 
        else:
            super().keyPressEvent(event)
            
    def start_scraping(self):
        chrome_driver_path = '/Users/lcy/Development/chromedriver'
        getty_url = self.url_input.text()
        keyword = self.keyword_input.text()

        self.getty_thread = GettyImagesThread(chrome_driver_path, getty_url, keyword)
        self.getty_thread.progress.connect(self.update_progress)
        self.getty_thread.finished.connect(self.on_getty_thread_finished)
        self.getty_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        
    def on_getty_thread_finished(self):
        print("Getty Images scraping thread finished")
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = GettyImagesTab()
    window.show()
    app.exec_()
