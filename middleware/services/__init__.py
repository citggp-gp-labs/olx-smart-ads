from backend.repository.gemini_image import GeminiImage
from backend.repository.gemini_text import GeminiPro
from backend.repository.api import Api


# Instance gemini model
gemini = GeminiPro(project="ciandt-gcp-partnership", location="us-east4", model="gemini-1.5-flash-002")

# Instance gemini image model
gemini_image = GeminiImage(project="ciandt-gcp-partnership", location="us-east4", model="gemini-1.5-flash-002")

categories_api = Api()
categories = categories_api.categories
