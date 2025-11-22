from fastapi import FastAPI
import uuid
import uvicorn

app = FastAPI()

cards = set()


@app.get("/ping")
def ping():
    return {"msg": "pong"}


@app.get('/generate_card')
def generate_card():
    # generate a random UUID, store it as string, and return JSON-serializable data
    id_str = str(uuid.uuid4())
    cards.add(id_str)
    return {"id": id_str}


if __name__ == "__main__":
    # Start the ASGI server when running `python app.py` directly
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)