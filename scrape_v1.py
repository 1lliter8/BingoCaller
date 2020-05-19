import urllib.request
from bs4 import BeautifulSoup
from tempfile import NamedTemporaryFile
import shutil
import csv


class URLScrape:
    def __init__(self, domain):
        self.domain = domain
        self.searchURL = 'https://www.google.com/search?q='
        # self.useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        self.useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
        self.headers = {'User-Agent': self.useragent}

    def googleNum(self, num):
        url = self.searchURL + "site:" + self.domain + '+' + '%22' + str(num) + '%22'
        html = ''

        request = urllib.request.Request(url, None, self.headers)
        response = urllib.request.urlopen(request)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        return soup.find('div', {'class': 'r'}).find('a', recursive=False)['href']

    def getTitle(self, url):
        html = ''

        request = urllib.request.Request(url, None, self.headers)
        response = urllib.request.urlopen(request)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')

        return title.string


class ScrapeWriter:
    def __init__(self, domain, filename):
        # ScrapeWriter('buzzfeed.com', 'buzzfeed.csv')
        # Expects a CSV with two columns, 'call' and 'number'
        # Call should have numbers

        self.domain = domain
        self.filename = filename
        self.tempfile = NamedTemporaryFile(mode = 'w', delete = False, encoding = 'utf8', newline = '')
        self.headers = ['number', 'call']
        self.scrape = URLScrape(self.domain)

    def updateCSV(self):
        try:
            with open(self.filename, 'r', encoding = 'utf8') as csvfile, self.tempfile:
                reader = csv.DictReader(csvfile, fieldnames = self.headers)
                writer = csv.DictWriter(self.tempfile, fieldnames = self.headers)

                for row in reader:
                    if row['call'] == '':
                        num = row['number']
                        url = self.scrape.googleNum(str(num))
                        title = self.scrape.getTitle(url)
                        row['number'], row['call'] = num, title

                    row = {'number': row['number'], 'call': row['call']}
                    writer.writerow(row)
        finally:
            shutil.move(self.tempfile.name, self.filename)


# buzz = ScrapeWriter('buzzfeed.com', 'buzzfeed.csv')
# buzz.updateCSV()

up = ScrapeWriter('upworthy.com', 'upworthy.csv')
up.updateCSV()