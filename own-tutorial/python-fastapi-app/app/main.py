from fastapi import FastAPI  
import os

app = FastAPI()   

@app.get("/") 
async def main_route():     
  custom_var = os.environ.get('CUSTOM_VAR', 'custom_var_default_value')
  return {"message": f"Hey, It is me, your friendly FastAPI K8s playground app. Custom var is set to '{custom_var}'"}

