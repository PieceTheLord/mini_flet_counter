from fastapi import FastAPI
from db.db import DB

app = FastAPI()

# root url
@app.get('/')
async def root():
  res = DB.get_count_value() 
  return res

@app.get('/plus')
async def plus():
  res = DB.plus_click_db()
  return res
 
@app.get('/minus')
async def minus():
  res = DB.minus_click_db()
  return res