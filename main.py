from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Naya import
from database import engine, Base
from users import router as users_router
from announcement import router as ann_router
from doubts import router as doubt_router
from materials import router as material_router 
from attendance import router as att_router

app = FastAPI()

# --- YE VALA HISSA ADD KARO ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Taki frontend backend se baat kar sake
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(ann_router)
app.include_router(doubt_router)
app.include_router(material_router) 
app.include_router(att_router, tags=["Attendance"])