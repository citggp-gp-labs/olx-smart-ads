import json
import os

from jinja2 import Environment, FileSystemLoader

from backend.repository.api import Api
from backend.repository.gemini_image import GeminiImage
from backend.repository.gemini_text import GeminiPro

# Instance gemini model
gemini = GeminiPro(
    project="ciandt-gcp-partnership", location="us-east4", model="gemini-1.5-flash-002"
)

# Instance gemini image model
gemini_image = GeminiImage(
    project="ciandt-gcp-partnership", location="us-east4", model="gemini-1.5-flash-002"
)

categories_api = Api()
categories = categories_api.categories
categories_dumped = json.dumps(categories, ensure_ascii=False)

prompts_dir = os.path.join(os.path.dirname(__file__), "..", "prompts")
env = Environment(loader=FileSystemLoader(prompts_dir))
template = env.get_template("prompts.txt")
