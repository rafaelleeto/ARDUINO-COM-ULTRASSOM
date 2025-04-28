import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host = "paparella.com.br",
        user = "paparell_prof",
        password = "@Senai2025",
        database = "paparell_python"
    )
    
def inserir_atualizar(dispositivo,valor):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    id_dispositivo = pegar_dispostivo()
    
    if not id_dispositivo:
        cursor.execute("""INSERT INTO dispositivos (aluno,dispositivo,valor) VALUES (%s,%s,%s)""",("Rafael Italiano",dispositivo,valor))
        print(f"Dados inseridos com sucesso no dispositivo {dispositivo} com o valor {valor}")
        
    else:
        cursor.execute("""UPDATE dispositivos SET valor=%s WHERE id=%s  """,(valor,id_dispositivo[0]))
        print(f"Dados atualizados com sucesso no dispositivo {dispositivo} com o valor {valor}")   
        
    conexao.commit()
    cursor.close()
    
def pegar_dispostivo():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT id FROM dispositivos WHERE aluno=%s """,("Rafael Italiano",))
    return cursor.fetchone()

def listar():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM dispositivos  """)
    return cursor.fetchall()
