# API de Livros — CRUD com Flask e MySQL

## Descrição

Esta API RESTful foi desenvolvida em Python utilizando Flask e MySQL para gerenciar um catálogo de livros. Permite operações básicas de **CRUD** (Criar, Ler, Atualizar e Deletar) livros, com autenticação por token para acesso seguro.

O projeto inclui tanto o servidor da API quanto um cliente Python para consumir os endpoints, servindo como exemplo completo de desenvolvimento backend e consumo de API.

---

## Funcionalidades

- Listar todos os livros cadastrados
- Buscar livro por ID
- Adicionar novo livro
- Atualizar livro existente
- Remover livro pelo ID
- Autenticação simples via token no cabeçalho HTTP

---

## Tecnologias utilizadas

- Python 3.x
- Flask
- MySQL
- mysql-connector-python
- requests (cliente HTTP em Python)
- python-dotenv (para variáveis de ambiente)

---

## Pré-requisitos

- Python 3 instalado
- MySQL instalado e configurado
- Git (opcional para clonar o projeto)

---

## Instalação e configuração

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/api-livros.git
cd api-livros
````

2. Crie um banco de dados MySQL chamado `biblioteca` e a tabela `livros`:

```sql
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE livros (
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL
);
```

Ou use o arquivo biblioteca.sql

3. Configure as variáveis de ambiente em `.env` ajustando os valores conforme seu ambiente:

```
BASE_URL=http://localhost:5000
API_TOKEN=meu_token_secreto_123

DB_HOST=localhost
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
DB_NAME=biblioteca
```

4. Instale as dependências do Python necessárias para o projeto:

```bash
pip install -r requirements.txt
```

5. Execute o servidor da API:

```bash
cd API_Server
python3 app.py
```

A API estará disponível em: `http://localhost:5000`

---

## Como usar a API?

### Autenticação

Todas as requisições devem conter o header:

```
Authorization: meu_token_secreto_123
```

---

### Endpoints

| Método | Endpoint     | Descrição               | Corpo da Requisição (JSON)                   |
| ------ | ------------ | ----------------------- | -------------------------------------------- |
| GET    | /livros      | Lista todos os livros   | —                                            |
| POST   | /livros      | Adiciona um novo livro  | `{ "id": int, "titulo": str, "autor": str }` |
| GET    | /livros/<id> | Busca livro pelo ID     | —                                            |
| PUT    | /livros/<id> | Atualiza dados do livro | `{ "titulo": str, "autor": str }`            |
| DELETE | /livros/<id> | Remove livro pelo ID    | —                                            |

---

### Exemplo de requisição com `curl`

Adicionar um livro:

```bash
curl -X POST http://localhost:5000/livros \
 -H "Authorization: meu_token_secreto_123" \
 -H "Content-Type: application/json" \
 -d '{"id":1, "titulo":"O Senhor dos Anéis", "autor":"J. R. R. Tolkien"}'
```

Buscar lista de livros:

```bash
curl -X GET http://localhost:5000/livros \
 -H "Authorization: meu_token_secreto_123"
```

---

## Melhorias futuras

* Implementar autenticação JWT para maior segurança
* Adicionar paginação e filtros na listagem de livros
* Desenvolver uma interface web para consumir a API

---

## Contato

\[Nícolas Tomaschewski Lopes] — \[[nicolas.tomaschewski@gmail.com](mailto:seu.email@example.com)]
Projeto disponível em: [https://github.com/seuusuario/api-livros](https://github.com/seuusuario/api-livros)

---
