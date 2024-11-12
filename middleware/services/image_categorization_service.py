from middleware.prompts import prompts
import json
from middleware.services import gemini_image

def run(data, categories_data):
    try:
        prompt = prompts.list_indication_prompt_v3(data['ad_title'], categories_data)

        response = gemini_image.generate(
            prompt=prompt, image_url=data['image_url'])

        json_response = response.text.replace("```", "").replace("json\n", "")
        categories_response = json.loads(json_response)

        categories_response['categories'] = [
            category for category in categories_response["categories"]
            if category['parent_id'] != category['category_id'] and category['parent_id'] is not None and category['category_id'] is not None
        ]

        log = {
            'url': 'v3/unified_categorization',
            'request': data,
            'response': categories_response,
        }

    except Exception as ex:
        print(ex)
        categories_response = {
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

    return categories_response
