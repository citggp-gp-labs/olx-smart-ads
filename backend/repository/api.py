import requests
import logging


class Api:
    def __init__(self):
        self.api_url = "https://ck-gw.olx.com.br/categories/simple"
        self.categories = []
        self.fetch_categories()

    def fetch_categories(self):
        """Fetch categories from API."""
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                self.categories = response.json()
            else:
                logging.error("Error calling the API: %s", response.status_code)
        except requests.exceptions.Timeout:
            logging.error("API call timed out")
