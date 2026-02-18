from fastapi import FastAPI

app = FastAPI(title="DevOps Showcase API")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Hello from AKS"}
