import urlparse
import pdfkit
from beautifulscraper import BeautifulScraper

BASE_URL = 'http://www.pythonweekly.com/archive/'
scraper = BeautifulScraper()
body = scraper.go(BASE_URL)

links = body.select('a')
reports_to_retrieve = [item.attrs['href'] for item in links if not item.attrs['href'].startswith('http')]
reports_to_scrape = [urlparse.urljoin(BASE_URL, item) for item in reports_to_retrieve]

if __name__ == "__main__":
    for url, f_name in  zip(reports_to_scrape, reports_to_retrieve):
        pdfkit.from_url(url, f_name.replace('html', 'pdf'))
