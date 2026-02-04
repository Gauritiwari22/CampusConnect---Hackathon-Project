from fastapi import FastAPI
from database import engine, Base
from users import router as users_router
from announcement import router as ann_router
from doubts import router as doubt_router
from materials import router as material_router # New

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(ann_router)
app.include_router(doubt_router)
app.include_router(material_router) # Registering