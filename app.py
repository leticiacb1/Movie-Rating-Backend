from fastapi import FastAPI
from backend.api import api

app = FastAPI()

# Registrar rotas:
app.include_router(api)

# Single path Application files (eg : React)
# ... 