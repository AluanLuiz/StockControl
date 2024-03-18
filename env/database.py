import config as cg

def create_DB(db_caminho):
    if not cg.os.path.exists(db_caminho):
        print("Banco de dados não encontrado. Criando...")

        # Conectar ao banco de dados (se não existir, ele será criado)
        conexao = cg.sql.connect(db_caminho)
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
                    qtde INTEGER NOT NULL,
                    id_local INTEGER,
                    id_fornecedor INTEGER,
                    FOREIGN KEY (id_local) REFERENCES Local(id_local),
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
            
            cursor.execute('''
                CREATE TABLE Local (
                    id_local INTEGER PRIMARY KEY AUTOINCREMENT,
                    z INTEGER NOT NULL,
                    x TEXT CHECK (length(x) = 1) NOT NULL,
                    y INTEGER NOT NULL
                )
            ''')
            
            # Inserir usuário mestre
            cursor.execute('''
                INSERT INTO Users (name_user, password, user_level)
                    VALUES (?, ?, ?)
                ''', ('Admin', 'Teste1', '4'))
            
            valores_z = list(range(1, 100))
            valores_x = list(cg.string.ascii_uppercase)
            valores_y = list(range(1, 100))
            
            for z in valores_z:
                for x in valores_x:
                    for y in valores_y:
                        cursor.execute('''
                            INSERT INTO Local (z, x, y)
                            VALUES (?, ?, ?)
                        ''', (z, x, y))
            
            # Salvar as alterações e fechar a conexão
            conexao.commit()
            conexao.close()
            
            print("Banco de dados e tabelas criados com sucesso.")
            
        except cg.sql.Error as e:
            print("Erro ao criar tabelas:", e)
            conexao.rollback()  # Desfaz quaisquer alterações pendentes
            conexao.close()
    else:
        print("Banco de dados encontrado. Verificando tabelas existentes...")
        # Conectar ao banco de dados existente
        conexao = cg.sql.connect(db_caminho)
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
                    quant_dispon INTEGER NOT NULL,
                    qtde INTEGER NOT NULL,
                    id_local INTEGER,
                    id_fornecedor INTEGER,
                    FOREIGN KEY (id_local) REFERENCES Local(id_local),
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
            
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Local'")
        if cursor.fetchone() is None:
            # Tabela Fornecedores não existe, criá-la
            cursor.execute('''
                CREATE TABLE Local (
                    id_local INTEGER PRIMARY KEY AUTOINCREMENT,
                    z INTEGER NOT NULL,
                    x TEXT NOT NULL CHECK (length(x) = 1),
                    y INTEGER NOT NULL
                )
            ''')
            
            valores_z = list(range(1, 100))
            valores_x = list(cg.string.ascii_uppercase)
            valores_y = list(range(1, 100))
            
            for z in valores_z:
                for x in valores_x:
                    for y in valores_y:
                        cursor.execute('''
                            INSERT INTO Local (z, x, y)
                            VALUES (?, ?, ?)
                        ''', (z, x, y))
        
            print("Tabela 'Local' criada.")
        
        conexao.commit()
        conexao.close()

# Caminho do banco de dados
db_caminho = 'env/db/control.db'

# Criar ou verificar se o banco de dados e as tabelas existem
create_DB(db_caminho)
