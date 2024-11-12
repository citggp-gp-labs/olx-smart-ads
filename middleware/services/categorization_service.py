from middleware.prompts import prompts
import json
from middleware.services import gemini

def run(data, categories):

    try:
        categorization = prompts.list_indication_prompt_v3(data['ad_title'], categories)

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