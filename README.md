# CRUD com POSTGRESQL + Python

Este projeto é um exemplo prático de CRUD usando:
- Banco de dados - **PostgreSQL**
- Conexao com **psycopg2**
- Interface web com **Streamlit**

### Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/kazukiwi/Aula-Postgresql.git
```

### 2. Criar um ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate #Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
crie um arquivo .env na raiz do projeto com:
DB_NAME=nome_banco
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

```bash
python -m streamlit run app.py
```

### Funcionalidades

- Conexão com o banco
- Criar alunos
- Listar alunos
- Atualizar alunos
- Deletar alunos
- Interface simples no streamlit

### Autor
Projeto desenvolvido em aula para treinar python + PostgreSQL

Professor: Gabriel Brito de Sousa