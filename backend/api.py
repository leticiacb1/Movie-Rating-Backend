from fastapi import APIRouter

from backend.endpoints import filmes
from backend.enums.tags import Tags

api = APIRouter(prefix='/api')

# Filmes
api.include_router(filmes.router , tags = [Tags.filmes])