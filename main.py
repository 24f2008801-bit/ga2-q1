from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware

import time

import uuid

app = FastAPI()

ALLOWED_ORIGIN = "https://dash-b48ubp.example.com"

# CORS FIRST

app.add_middleware(

    CORSMiddleware,

    allow_origins=[ALLOWED_ORIGIN],

    allow_credentials=False,

    allow_methods=["GET", "POST", "OPTIONS"],

    allow_headers=["*"],

)

# middleware SECOND

@app.middleware("http")

async def add_headers(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    response.headers["X-Request-ID"] = str(uuid.uuid4())

    response.headers["X-Process-Time"] = str(time.time() - start)

    return response

@app.get("/stats")

async def stats(values: str):

    nums = [int(x) for x in values.split(",")

]

    return {

        "email": "24f2008801@ds.study.iitm.ac.in",

        "count": len(nums),

        "sum": sum(nums),

        "min": min(nums),

        "max": max(nums),

        "mean": sum(nums) / len(nums)

    }

@app.get("/")

def home():

    return {"status": "running"}