from agno.models.mistral import MistralChat
from agno.models.google import Gemini
from agno.models.groq   import Groq
from dotenv import load_dotenv
from typing import Literal


load_dotenv()

class Model:
    def __init__(self,model:Literal['Gemini','Mistral','Groq']='Groq'):
            self.model_name=model
            if self.model_name not in ['Gemini','Mistral','Groq']:
                raise ValueError("Model not supported")
            


    def initialize_model(self):
          
          if self.model_name == 'Gemini':
              return Gemini()
          
          elif self.model_name == 'Mistral':
              return MistralChat()
         
          elif self.model_name == 'Groq':
              return Groq()
          

model=Model().initialize_model()

