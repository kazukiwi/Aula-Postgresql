from db import conectar

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:  
        try:
            cursor.execute("""
        INSERT INTO alunos (nome, idade)
        VALUES (%s, %s)
        """, (nome, idade))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir o aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_aluno():
    conexao, cursor = conectar()
    if conexao:  
        try:
            cursor.execute("""
        SELECT * FROM alunos ORDER BY id
        """)
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os alunos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

