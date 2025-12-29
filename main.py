from fastapi import FastAPI
from configs.constants import APP_TITLE,APP_DESCRIPTION,APP_VERSION,ALLOW_CREDENTIALS,ALLOW_HEADERS,ALLOW_METHODS,ALLOW_ORIGINS,API,API_VERSION
from fastapi.middleware.cors import CORSMiddleware
from routers.todos_api_routes import router as todo_router
from routers.todos_web_routes import router as web_router
from database.initializer import DatabaseInitializer
from fastapi.staticfiles import StaticFiles
from database.connectors.sqlite import SQLiteConnector



app:FastAPI = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.on_event("startup")
def startup_event():
    connector = SQLiteConnector()
    DatabaseInitializer(connector=connector).initialize_schema()


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)


PREFIX:str = f"{API}/{API_VERSION}"


app.include_router(router=todo_router,prefix=PREFIX)
app.include_router(router=web_router)






