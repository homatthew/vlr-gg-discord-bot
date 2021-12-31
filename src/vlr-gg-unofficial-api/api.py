from fastapi import FastAPI
import requests
app = FastAPI(
  title="vlr-gg-api",
  description="An Unofficial REST API for [vlr.gg](https://www.vlr.gg/), a site for Valorant Esports match and news coverage.",
)

@app.get("/ping")
async def ping():
  return "pong"
