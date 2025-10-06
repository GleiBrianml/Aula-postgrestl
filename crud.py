from db import conectar

def criar_aluno(nome,idade):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome,idade) VALUES (%s,%s)",
                (nome,idade)
                        )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()
def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM alunos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar listar alunos: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_idade(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar a idade: {erro}")
        finally:
            cursor.close()
            conexao.close()

