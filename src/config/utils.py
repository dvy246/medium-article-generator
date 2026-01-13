from agno.models.mistral import MistralChat
from agno.models.google import Gemini
from agno.models.openrouter import OpenRouter
from agno.models.groq   import Groq
from dotenv import load_dotenv
from typing import Literal


load_dotenv()

class Model:
    def __init__(self,model:Literal['Gemini','Mistral','Groq','Open']='Open'):
            self.model_name=model
            if self.model_name not in ['Gemini','Mistral','Groq','Open']:
                raise ValueError("Model not supported")
            


    def initialize_model(self):
          
          if self.model_name == 'Gemini':
              return Gemini()
          
          elif self.model_name == 'Mistral':
              return MistralChat()
         
          elif self.model_name == 'Groq':
              return Groq()
          
          elif self.model_name == 'Open':
              return OpenRouter()
         
          else:
              raise ValueError("Model not supported")
          

model=Model('Mistral').initialize_model()

