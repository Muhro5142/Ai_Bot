import json
import time
import base64
from PIL import Image
from io import BytesIO
import requests
import telebot

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

    def decode64(self,base64_img,):
        
        for i in range(len(base64_img)):
            image_data = base64.b64decode(base64_img[i])
        
            image = Image.open(BytesIO(image_data))
            image.save(f'output{i}.png' )  # Сохранение в файл
            


        
if __name__ == '__main__':
    promt = input("""
$$$$$$$\  $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\         $$$$$$\  $$$$$$\ 
$$  __$$\ $$ |  $$ |$$  __$$\\__$$  __|$$  __$$\       $$  __$$\ \_$$  _|
$$ |  $$ |$$ |  $$ |$$ /  $$ |  $$ |   $$ /  $$ |      $$ /  $$ |  $$ |  
$$$$$$$  |$$$$$$$$ |$$ |  $$ |  $$ |   $$ |  $$ |      $$$$$$$$ |  $$ |  
$$  ____/ $$  __$$ |$$ |  $$ |  $$ |   $$ |  $$ |      $$  __$$ |  $$ |  
$$ |      $$ |  $$ |$$ |  $$ |  $$ |   $$ |  $$ |      $$ |  $$ |  $$ |  
$$ |      $$ |  $$ | $$$$$$  |  $$ |    $$$$$$  |      $$ |  $$ |$$$$$$\ 
\__|      \__|  \__| \______/   \__|    \______/       \__|  \__|\______|
                                                                         
                                                                         
                                                                         
Приветсвую Пользователь!
вводи какую картинку ты хочешь а я тебе ее нарискую!:

""")
    
    
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'A9933FF3DACB02861250B77685B40903', 'EFB5C82E5A63D34116EAB6CF762695B0')
    model_id = api.get_model()
    uuid = api.generate(promt, model_id)
    base64_img = api.check_generation(uuid)
    api.decode64(base64_img)
    
        
       
    

#Don't forget to specify exactly YOUR_KEY and YOUR_SECRE