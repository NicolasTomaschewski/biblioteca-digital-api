import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from utils import testar_endpoints_livros
from API_Server.config import BASE_URL, API_TOKEN

if testar_endpoints_livros():
    novo_livro = {
        'id': 4,
        'titulo': 'O teste',
        'autor': 'J. R. R. Tolkien'
    }

    url = f'{BASE_URL}/livros'
    headers = {'Authorization': API_TOKEN}

    response = requests.post(url, json=novo_livro, headers=headers)

    print('\n📘 Novo livro adicionado:')
    print(f'Status Code: {response.status_code}')
    print(response.json())
else:
    print('⚠️ API indisponível. Não foi possível adicionar o livro.')
