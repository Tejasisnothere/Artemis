from intent_extractor.constants.application import AUDIO_DATA_PATH
import requests
import os


class AudioIngestor:
    def __init__(self, url=None, filename=None):
        self.url = url
        self.filename = filename
        
       

    def loadURL(self):
        url = self.url
        resp = requests.get(url=url)
        
        flag = True
        audio_path = None


        if resp.status_code == 200:
            with open(audio_path, "wb") as f:
                f.write(resp.content)
            
            
        else:
            
            flag = False
        
        
        return flag

    def loadFile(self):
        
        audio_path = os.path.join(AUDIO_DATA_PATH, self.filename)

        return audio_path
    
    def load(self):
        if(self.url):
            self.loadURL()
        else:
            return self.loadFile()
    
