from fastapi import FastAPI, Depends
from .config import get_settings, Settings

# Create a new instance of FastAPI and set up a synchronous sanity check route
app = FastAPI()


# Here, the Depends function is a dependency that declares another dependency,
# get_settings. Put another way, Depends depends on the result of get_settings.
# The value returned, Settings, is then assigned to the settings parameter.
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
