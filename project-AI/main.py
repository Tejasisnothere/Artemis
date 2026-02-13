from fastapi import FastAPI, Request
import pandas as pd
from intent_extractor.pipeline.ingestor.text_ingestor import TextIngestor
from intent_extractor.pipeline.model.audio_transcription import Transcribe
from intent_extractor.pipeline.model.trans import Trans
from langdetect import detect

app = FastAPI()


german = "https://drive.google.com/uc?export=download&id=1I59G7h153pDxzmwfBrlku6Dm9lv8p-GI"
english = "https://drive.google.com/uc?export=download&id=1RVObKS8mFEa9vguC2rTn_PFAJsC8gGqR"


@app.post('/test-endpoint')
async def get_json(request: Request):
    array = await request.json()
    json_arr = array['json_array']
    TextIng = TextIngestor(json_arr=json_arr, filename='loaded.csv')
    TextIng.save_file()
    

@app.post('/test-transcriber')
async def transcribe(request: Request):
    data = await request.json()

    url = data['url']
   
    T = Transcribe(url)

    extract = T.transcribe_text()

    if(detect(extract[:int(len(extract)/2)]) == 'en'):
        pass
    else:


        print("\n\n\n")
        
        transtext = Trans(extract)

        await transtext.translate_text()
    
