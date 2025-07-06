import requests
from API_Server.config import BASE_URL, API_TOKEN

def testar_endpoint(url: str) -> bool:
    headers = {'Authorization': API_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f'✅ [200 OK] Conexão com a API funcionando: {url}')
            return True
        else:
            print(f'❌ [Erro {response.status_code}] no endpoint: {url}')
            return False
    except requests.exceptions.RequestException as e:
        print(f'❌ [Falha de Conexão] {url} - Erro: {e}')
        return False

def testar_endpoints_livros() -> bool:
    url = f'{BASE_URL}/livros'
    print('\n🔹 Testando Conexão com endpoint de livros')
    return testar_endpoint(url)
