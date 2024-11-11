from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v3/unified_categorization")
def unified_categorization_v3(request: Request):
    data = request.json
    print(data)
    return {"payload": data}
