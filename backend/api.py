from fastapi import FastAPI

app = FastAPI()#インスタンス化

@app.get("/")#ルーティング　@はdecorator
async def index():
    return {"message":"FastAPIだぞ"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)