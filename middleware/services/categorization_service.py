import os
from jinja2 import Environment, FileSystemLoader
from middleware.prompts import prompts
import json
from middleware.services import gemini

async def run(data, categories):

    try:
        prompts_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
        env = Environment(loader=FileSystemLoader(prompts_dir))
        template = env.get_template('prompts.txt')
        categorization = template.render({"categories": categories, "description" : data['ad_title']})

        categorization_response = gemini.gemini_pro(prompt=categorization).text

        categories_json = categorization_response.replace("```", "").replace("json\n", "")
        categories = json.loads(categories_json)

        categories['categories'] = [
            category for category in categories["categories"]
            if category['parent_id'] != category['category_id'] and category['parent_id'] is not None and category['category_id'] is not None
        ]

    except Exception as ex:
        print(ex)
        categories = {
            "categories": [
                {
                    "category_id": 0,
                    "category_main_name": "Erro",
                    "category_name": "Erro",
                    "parent_id": 0,
                    "probability": 0
                }
            ]
        }

    return categories