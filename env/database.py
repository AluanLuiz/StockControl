import sqlite3 as sql
import os

def create_DB(db_caminho):
    if not os.path.exists(db_caminho):
        print("Banco de dados não encontrado. Criando...")

        # Conectar ao banco de dados (se não existir, ele será criado)
        conexao = sql.connect(db_caminho)
        cursor = conexao.cursor()

        # Criar tabelas
        try:
            cursor.execute('''
                CREATE TABLE Users (
                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_user TEXT NOT NULL,
                    password TEXT NOT NULL,
                    user_level TEXT DEFAULT '1' NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE Products (
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
                CREATE TABLE Fornecedores (
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
        except sql.Error as e:
            print("Erro ao criar tabelas:", e)
            conexao.rollback()  # Desfaz quaisquer alterações pendentes
            conexao.close()
    else:
        print("Banco de dados encontrado. Verificando tabelas existentes...")
        # Conectar ao banco de dados existente
        conexao = sql.connect(db_caminho)
        cursor = conexao.cursor()

        # Verificar se as tabelas existem
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
        if cursor.fetchone() is None:
            # Tabela Users não existe, criá-la
            cursor.execute('''
                CREATE TABLE Users (
                    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_user TEXT NOT NULL,
                    password TEXT NOT NULL,
                    user_level TEXT DEFAULT '1' NOT NULL
                )
            ''')
            
            cursor.execute('''
                INSERT INTO Users (name_user, password, user_level)
                    VALUES (?, ?, ?)
                ''', ('Admin', 'Teste1', '4'))
            
            print("Tabela 'Users' criada.")
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Products'")
        if cursor.fetchone() is None:
            # Tabela Products não existe, criá-la
            cursor.execute('''
                CREATE TABLE Products (
                    id_prod INTEGER PRIMARY KEY AUTOINCREMENT,
                    bar_code TEXT NOT NULL,
                    name_simple TEXT NOT NULL,
                    description TEXT NOT NULL,
                    quantidade_disponivel INTEGER NOT NULL,
                    Local_arm TEXT NOT NULL CHECK (length(Local_arm) <= 4),
                    source_price REAL,
                    id_fornecedor INTEGER,
                    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores(id_fornecedor)
                )
            ''')
            print("Tabela 'Products' criada.")
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Fornecedores'")
        if cursor.fetchone() is None:
            # Tabela Fornecedores não existe, criá-la
            cursor.execute('''
                CREATE TABLE Fornecedores (
                    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    cnpj TEXT NOT NULL,
                    contato TEXT NOT NULL
                )
            ''')
            print("Tabela 'Fornecedores' criada.")
        
        conexao.commit()
        conexao.close()
