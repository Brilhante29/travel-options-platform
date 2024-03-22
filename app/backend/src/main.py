from fastapi import FastAPI
from src.infra.database.sqlite .init_db import init_db
from src.infra.rest.routes.router import api_router

app = FastAPI()

app.include_router(api_router)


init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)