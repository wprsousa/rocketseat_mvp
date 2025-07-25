import uvicorn
from src.main.server.server import app


if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=3000, reload=True)
