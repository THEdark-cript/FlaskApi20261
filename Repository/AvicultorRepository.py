from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Avicultor.
'''

class AvicultorRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Buscando todos os avicultores.")
        cursor.execute("SELECT * FROM tb_avicultor")
        return cursor.fetchall()

    def getByIdAvicultor(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Buscando avicultor pelo id {id}.")
        cursor.execute("SELECT * FROM tb_avicultor WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, nascimento, cpf, caf):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Inserindo novo avicultor.")
        cursor.execute(
            "INSERT INTO tb_avicultor(nome, nascimento, cpf, caf) VALUES(%s, %s, %s, %s) RETURNING id",
            (nome, nascimento, cpf, caf)
        )
        conn.commit()
        return cursor.fetchone()[0]  

    def update(self, id, nome, nascimento, cpf, caf):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Atualizando avicultor {id}.")
        cursor.execute(
            "UPDATE tb_avicultor SET nome=%s, nascimento=%s, cpf=%s, caf=%s WHERE id=%s",
            (nome, nascimento, cpf, caf, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Deletando avicultor {id}.")
        cursor.execute("DELETE FROM tb_avicultor WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
