from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes.predict import router as today_router
from app.routes.prix import router as prix_router
from app.routes.region import router as region_router

app = FastAPI(title="API Prix Pompe")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(today_router)
app.include_router(prix_router)
app.include_router(region_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory="templates", html=True), name="templates")
