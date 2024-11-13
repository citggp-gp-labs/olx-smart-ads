import os
import logging
from fastapi import FastAPI, Request

import middleware.services.categorization_service as categorization_service
import middleware.services.image_categorization_service as image_categorization_service
from middleware.services import categories_dumped

app = FastAPI()

log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()

level_mapping = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

log_level_numeric = level_mapping.get(log_level, logging.INFO)

logging.getLogger().setLevel(log_level_numeric)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/v3/unified_categorization")
async def unified_categorization_v3(request: Request):
    data = await request.json()
    if not data.get("image_url"):
        return await categorization_service.run(data, categories_dumped)
    else:
        return await image_categorization_service.run(data, categories_dumped)
