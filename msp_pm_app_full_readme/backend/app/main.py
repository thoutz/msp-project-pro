
from fastapi import FastAPI
from app.routers import auth, tickets

app = FastAPI(title="MSP PM App")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tickets.router, prefix="/tickets", tags=["Tickets"])

@app.get("/")
def root():
    return {"status": "ok"}
