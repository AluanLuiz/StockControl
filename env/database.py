import sqlite3 as sql
import os

def create_DB(db_path):
    if not os.path.exists(db_path):
        print("Banco de dados não encontrado. Criando...")

        # Conectar ao banco de dados (se não existir, ele será criado)
        conexao = sql.connect(db_path)
        cursor = conexao.cursor()

        # Criar tabelas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                name_user TEXT NOT NULL,
                password TEXT NOT NULL,
                user_level TEXT DEFAULT '1' NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
                bar_code TEXT NOT NULL,
                name_simple TEXT NOT NULL,
                description TEXT NOT NULL,
                quantidade_disponivel INTEGER NOT NULL,
                sale_price REAL NOT NULL,
                source_price REAL,
                id_fornecedor INTEGER,
                FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores(id_fornecedor)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Fornecedores (
                id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cnpj TEXT NOT NULL,
                contato TEXT NOT NULL
            )
        ''')
        
        # Inserir usuário mestre
        cursor.execute('''
            INSERT INTO Users (name_user, password, user_level)
                VALUES (?, ?, ?)
            ''', ('Admin', 'Teste1', '4'))
        
        # Salvar as alterações e fechar a conexão
        conexao.commit()
        conexao.close()
        
        print("Banco de dados e tabelas criados com sucesso.")
    else:
        print("Banco de dados já existe.")
