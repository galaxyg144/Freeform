from fastapi import FastAPI

app = FastAPI(title="Freeform Music API")

@app.get("/")
def root():
    return {"status": "Freeform Music API running"}
