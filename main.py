from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v3/unified_categorization")
async def unified_categorization_v3(request: Request):
    data = await request.json
    print(data)
    return {"payload": data}
