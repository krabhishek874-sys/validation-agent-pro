import requests
from config import *

def get_validations():
    try:
        url=f"{SERVICENOW_INSTANCE}/api/now/table/u_validation_tracker"
        r=requests.get(url,auth=(SERVICENOW_USER,SERVICENOW_PASSWORD))
        return r.json().get("result",[])
    except Exception:
        return []
