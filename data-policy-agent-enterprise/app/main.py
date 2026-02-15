from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, policy
from app.utils.logger import logger

app = FastAPI(title="Data Policy Agent", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(policy.router)

@app.on_event("startup")
async def startup():
    logger.info("Application starting...")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Application shutting down...")
