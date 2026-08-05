from helpers.database import get_conn
from helpers.logger import logger

class AviarioRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Buscando todos os aviários.")
        cursor.execute("SELECT * FROM tb_aviario")
        return cursor.fetchall()

    def getById(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Buscando aviário pelo id {id}.")
        cursor.execute("SELECT * FROM tb_aviario WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Inserindo novo aviário.")
        cursor.execute(
            "INSERT INTO tb_aviario (nome, capacidade) VALUES (%s, %s) RETURNING id",
            (nome, capacidade)
        )
        conn.commit()
        return cursor.fetchone()[0]

    def update(self, id, nome, capacidade):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Atualizando aviário {id}.")
        cursor.execute(
            "UPDATE tb_aviario SET nome=%s, capacidade=%s WHERE id=%s",
            (nome, capacidade, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Deletando aviário {id}.")
        cursor.execute("DELETE FROM tb_aviario WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
