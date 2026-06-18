from fastapi import FastAPI

from api.routers import claim, risk, monitoring

app =  FastAPI(title="Healthcare ML API")

@app.get("/")
def root():
    return {"message": "Healthcare ML API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Resgistering the routers /predisction/risk
app.include_router(risk.router, prefix="/predict", tags=["Risk score prodiction"])
app.include_router(claim.router, prefix="/predict", tags=["Claim status prodiction"])
app.include_router(monitoring.router, prefix="/monitor", tags=["Monitoring"])
