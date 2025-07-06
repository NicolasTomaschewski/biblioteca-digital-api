import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from utils import testar_endpoints_livros
from API_Server.config import BASE_URL, API_TOKEN


if testar_endpoints_livros():
    url = f'{BASE_URL}/livros'
    headers = {'Authorization': API_TOKEN}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        livros = response.json()
        print('\n📚 Lista de livros:')
        print(f'Status Code: {response.status_code}\n')

        if livros:
            for livro in livros:
                print(f'ID: {livro["id"]}')
                print(f'Título: {livro["titulo"]}')
                print(f'Autor: {livro["autor"]}')
                print('-' * 40)
        else:
            print('Nenhum livro encontrado.')
    else:
        print(f'❌ Erro ao obter lista de livros. Código de status: {response.status_code}')
else:
    print('⚠️ API indisponível. Não foi possível obter a lista de livros.')
