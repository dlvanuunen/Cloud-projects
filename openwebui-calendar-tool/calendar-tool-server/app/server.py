# app/main.py
import os, hmac
from fastapi import FastAPI, Depends, Header, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer = HTTPBearer()

import  calendar_tools  as ct 
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(title= "Calendar Tool API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],   # your Open WebUI address
#     allow_methods=["GET", "OPTIONS"],
#     allow_headers=["*"],
# )


# This is an authentication function that checks a header against a .env variable (api_key)
def authenticate_header(api_key: str = Header(...)):
    if api_key!=os.getenv("API_KEY"):
            raise HTTPException(401)


def authenticate_bearer(creds: HTTPAuthorizationCredentials = Depends(bearer)):
    if not hmac.compare_digest(creds.credentials, os.environ["API_KEY"]):
        raise HTTPException(status_code=401, detail="Invalid token")


# AUth

@app.get("/events", dependencies=[Depends(authenticate_bearer)],  operation_id="daemonal_calendar_events", summary="Returns calendar events between start and end date (ISO datetime format) [in testing between now and +7 days]")
def daemonal_calendar_events():
    json = ct.fetch_events()
    return json
    

# No AUth for testing purpose
# @app.get("/events", operation_id="D_list_calendar_events", summary="Returns calendar events between start and end date (ISO datetime format) [in testing between now and +7 days]")
# def list_events():
#     json = ct.fetch_events()
#     return json
    