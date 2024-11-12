from fastapi import FastAPI, Request
import middleware.services.categorization_service as categorization_service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v3/unified_categorization")
async def unified_categorization_v3(request: Request):
    data = await request.json
    # chamar a api de categorias aqui, e passar por parametro
    return categorization_service.run(data, "")
