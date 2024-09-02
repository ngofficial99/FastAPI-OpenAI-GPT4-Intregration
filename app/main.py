from fastapi import FastAPI


# Initalize Fast API
app = FastAPI()

@app.get("/ok")
async def ok_endpoint():
    return{"message":"ok"}