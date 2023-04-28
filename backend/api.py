from fastapi import APIRouter

from backend.routers import filmes , avaliacoes
from backend.enums.tags import Tags

api = APIRouter(prefix='/api')

# Filmes
api.include_router(filmes.router , tags = [Tags.filmes])

# Avaliacoes
# api.include_router(avaliacoes.router , tags = [Tags.avaliacoes])