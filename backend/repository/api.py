from app.services.models import GeminiPro
import requests
import os
from app.services.models_image import GeminiImage

class api:
    def __init__(self):
        self.API_URL = "https://ck-gw.olx.com.br/categories/simple"
        self.categories = []
        self.gemini = None
        self.gemini_image = None
        self.run()

    def fetch_categories(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            self.categories = response.json()
        else:
            #todo - implementaion of logging logic
            #logging.error(f"Error calling the API: {response.status_code}")

    def initialize_gemini_models(self):
        self.gemini = GeminiPro(project=os.getenv('PROJECT_ID'), location=os.getenv('PROJECT_LOCATION'), model=os.getenv('DEFAULT_MODEL_VERSION'))
        self.gemini_image = GeminiImage(project=os.getenv('PROJECT_ID'), location=os.getenv('PROJECT_LOCATION'), model=os.getenv('DEFAULT_MODEL_VERSION'))

    def run(self):
        self.fetch_categories()
        self.initialize_gemini_models()
