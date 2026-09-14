import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key:
    print("Variável API_KEY lida com sucesso!")
else:
    print("Não foi possível encontrar a variável API_KEY.")