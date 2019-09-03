import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from html.parser import HTMLParser
import re


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def main():
    page = Page(
        'https://haku.yle.fi/?query=morgonkollen&type=article&uiLanguage=sv')
    soup = bs.BeautifulSoup(page.html, 'html.parser')

    links = (soup.find('a', class_='ArticleResults__A-sc-858ijy-1 ffOqVh', href=True))
    print(links)
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(links))
    print("Original string: ", links)
    print("Urls: ", urls)


if __name__ == '__main__':
    main()
