from agno.models.mistral import MistralChat
from agno.models.google import Gemini
from dotenv import load_dotenv
from typing import Literal


load_dotenv()

class Model:
    def __init__(self,model:Literal['Gemini','Mistral']='Mistral'):
            self.model_name=model
            if self.model_name not in ['Gemini','Mistral']:
                raise ValueError("Model not supported")
            


    def initialize_model(self):
          
          if self.model_name == 'Gemini':
              return Gemini()
          
          elif self.model_name == 'Mistral':
              return MistralChat()
          

model=Model(model='Gemini')