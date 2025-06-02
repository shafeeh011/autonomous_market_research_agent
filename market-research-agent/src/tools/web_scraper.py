from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch page: {url} with status code: {response.status_code}")

    def parse_html(self, html_content):
        return BeautifulSoup(html_content, 'html.parser')

    def scrape_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        html_content = self.fetch_page(url)
        soup = self.parse_html(html_content)
        return self.extract_data(soup)

    def extract_data(self, soup):
        # Placeholder for data extraction logic
        data = {}
        # Example: Extracting title
        data['title'] = soup.title.string if soup.title else 'No title found'
        return data

    def scrape_multiple_endpoints(self, endpoints):
        results = {}
        for endpoint in endpoints:
            results[endpoint] = self.scrape_data(endpoint)
        return results
