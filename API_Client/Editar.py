import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from utils import testar_endpoints_livros
from API_Server.config import BASE_URL, API_TOKEN

if testar_endpoints_livros():
    livro_id = 4
    dados_atualizados = {
        'titulo': 'As Duas Torres - Edição Revisada',
        'autor': 'J. R. R. Tolkien'
    }

    url = f'{BASE_URL}/livros/{livro_id}'
    headers = {'Authorization': API_TOKEN}

    response = requests.put(url, json=dados_atualizados, headers=headers)

    print(f'\n🔁 Livro ID {livro_id} atualizado:')
    print(f'Status Code: {response.status_code}')
    print(response.json())
else:
    print('⚠️ API indisponível. Não foi possível atualizar o livro.')
