from fastapi import FastAPI
from fastapi.responses import FileResponse

index_path = "index.html"
app = FastAPI()


@app.get('/')
async def root():
    return FileResponse(index_path)


