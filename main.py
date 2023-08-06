import sys
from PyQt5.QtWidgets import QApplication, QTabWidget
from ImageScrape.Tabs.InstagramTab import InstagramTab
from ImageScrape.Tabs.GettyImagesTab import GettyImagesTab

class ScraperApp(QTabWidget):
    def __init__(self):
        super().__init__()

        instagram_tab = InstagramTab()
        getty_images_tab = GettyImagesTab()

        self.addTab(getty_images_tab, "Getty Images")
        self.addTab(instagram_tab, "Instagram")

        self.setWindowTitle("Scraper App")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScraperApp()
    window.show()
    sys.exit(app.exec_())
