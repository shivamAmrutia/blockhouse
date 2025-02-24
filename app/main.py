from fastapi import FastAPI
from .routes import order, websocket
from .database import engine
from . import models

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routes
app.include_router(order.router)
app.include_router(websocket.router)