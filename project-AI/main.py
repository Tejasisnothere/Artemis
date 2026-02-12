from fastapi import FastAPI, Request
import pandas as pd
from intent_extractor.pipeline.ingestor.text_ingestor import TextIngestor


app = FastAPI()

@app.post('/test-endpoint')
async def get_json(request: Request):
    array = await request.json()
    json_arr = array['json_array']
    TextIng = TextIngestor(json_arr=json_arr, filename='loaded.csv')
    TextIng.save_file()
    

    
    
