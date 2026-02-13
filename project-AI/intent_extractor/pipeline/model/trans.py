from googletrans import Translator
import asyncio



class Trans:
    def __init__(self, text):
        self.text = text
    
    async def translate_text(self):
        async with Translator() as translator:
            result = await translator.translate(self.text)

            print(result)

            return result