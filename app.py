from  fastapi  import  FastAPI
from  backend . api  import  api

app  =  FastAPI ()

# Register routes:
app . include_router ( api )

# Single path Application files (eg : React)
# ...