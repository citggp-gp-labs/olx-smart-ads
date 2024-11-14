import json
import os
from jinja2 import Environment, FileSystemLoader

from backend.repository.api import Api
from backend.repository.gemini_image import GeminiImage
from backend.repository.gemini_text import GeminiPro
import backend.core.config as config

config.load()

print(f"Nome do modelo: {os.getenv('DEFAULT_MODEL_VERSION')}")

# Instance gemini model
gemini = GeminiPro(
    project=os.getenv('PROJECT_ID'),
    location=os.getenv('PROJECT_LOCATION'),
    model=os.getenv('DEFAULT_MODEL_VERSION')
)

# Instance gemini image model
gemini_image = GeminiImage(
    project=os.getenv('PROJECT_ID'),
    location=os.getenv('PROJECT_LOCATION'),
    model=os.getenv('DEFAULT_MODEL_VERSION')
)

categories_api = Api()
categories = categories_api.categories
categories_dumped = json.dumps(categories, ensure_ascii=False)

prompts_dir = os.path.join(os.path.dirname(__file__), "..", "prompts")
env = Environment(loader=FileSystemLoader(prompts_dir))
template = env.get_template("prompts.txt")
