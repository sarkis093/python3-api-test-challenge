import os
from  dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv('API_KEY')
