import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')



def get_model_client():
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=api_key
    )
    return model_client