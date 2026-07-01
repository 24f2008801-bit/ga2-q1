from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid

app = FastAPI()

ALLOWED_ORIGIN = "https://dash-b48ubp.example.com"

# Strict CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for custom headers
@app.middleware("http")
async def add_headers(request: Request, call_next):
    start = time.time()
    response = await call_next(request)

    process_time = time.time() - start
    response.headers["X-Request-ID"] = str(uuid.uuid4())
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.get("/stats")
async def stats(values: str):
    nums = [int(x) for x in values.split(",")]

    return {
        "email": "24f2008801@ds.study.iitm.ac.in",
        "count": len(nums),
        "sum": sum(nums),
        "min": min(nums),
        "max": max(nums),
        "mean": sum(nums) / len(nums)
    }