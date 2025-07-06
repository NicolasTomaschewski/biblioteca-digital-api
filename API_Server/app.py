from flask import Flask, jsonify, request
from functools import wraps
from db import conectar
import mysql.connector

app = Flask(__name__)

TOKEN = "meu_token_secreto_123"

def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'mensagem': 'Token está faltando!'}), 401
        if token != TOKEN:
            return jsonify({'mensagem': 'Token inválido!'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET'])
def boas_vindas():
    return 'Hello, World!'

@app.route('/livros', methods=['GET'])
@token_obrigatorio
def obter_livros():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
@token_obrigatorio
def obter_livro(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livros WHERE id = %s", (id,))
    livro = cursor.fetchone()
    cursor.close()
    conexao.close()
    if livro:
        return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado!'}), 404

@app.route('/livros/<int:id>', methods=['PUT'])
@token_obrigatorio
def editar_livro_id(id):
    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE livros SET titulo=%s, autor=%s WHERE id=%s",
                   (dados['titulo'], dados['autor'], id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'mensagem': 'Livro atualizado com sucesso'})

@app.route('/livros', methods=['POST'])
@token_obrigatorio
def incluir_novo_livro():
    novo_livro = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO livros (id, titulo, autor) VALUES (%s, %s, %s)",
                       (novo_livro['id'], novo_livro['titulo'], novo_livro['autor']))
        conexao.commit()
        return jsonify(novo_livro), 201
    except mysql.connector.IntegrityError:
        return jsonify({'erro': 'ID já existente'}), 400
    finally:
        cursor.close()
        conexao.close()

@app.route('/livros/<int:id>', methods=['DELETE'])
@token_obrigatorio
def excluir_livro(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livros WHERE id = %s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'mensagem': 'Livro excluído com sucesso!'})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
