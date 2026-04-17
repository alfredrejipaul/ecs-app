from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from Alfred's ECS deployment",
        "container": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "production"),
    }

