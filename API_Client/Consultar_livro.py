import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import testar_endpoints_livros
from API_Server.config import BASE_URL, API_TOKEN
import requests

if testar_endpoints_livros():
    livro_id = 2
    url = f'{BASE_URL}/livros/{livro_id}'
    headers = {'Authorization': API_TOKEN}

    response = requests.get(url, headers=headers)

    print(f'\n📘 Resultado da busca por livro com ID {livro_id}:')
    print(f'Status Code: {response.status_code}')
    print(response.json())
else:
    print('⚠️ Não foi possível conectar à API. Dados não serão exibidos.')
