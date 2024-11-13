import json
import logging
from middleware.services import gemini, template


async def run(data, categories):
    try:
        categorization = template.render(
            {"categories": categories, "description": data["ad_title"]}
        )

        categorization_response = await gemini.gemini_pro(prompt=categorization)

        categories_json = categorization_response.text.replace("```", "").replace(
            "json\n", ""
        )

        # isso pesa demais o código, revisar
        categories = json.loads(categories_json)

        categories["categories"] = [
            category
            for category in categories["categories"]
            if category["parent_id"] != category["category_id"]
            and category["parent_id"] is not None
            and category["category_id"] is not None
        ]

        log = {
            'url': 'v3/unified_categorization',
            'request': data,
            'response': categorization_response,
        }
        logging.info(log)

    # tratar melhor as exceções, não deixar genérico assim
    except Exception as ex:
        logging.error(ex)
        categories = {
            "categories": [
                {
                    "category_id": 0,
                    "category_main_name": "Erro",
                    "category_name": "Erro",
                    "parent_id": 0,
                    "probability": 0,
                }
            ]
        }

    return categories
