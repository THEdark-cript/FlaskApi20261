from helpers.database import get_conn
from helpers.logger import logger

class GalpaoRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Buscando todos os galpões.")
        cursor.execute("SELECT * FROM tb_galpao")
        return cursor.fetchall()

    def getById(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Buscando galpão pelo id {id}.")
        cursor.execute("SELECT * FROM tb_galpao WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, nome, capacidade, tipo):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Inserindo novo galpão.")
        cursor.execute(
            "INSERT INTO tb_galpao (nome, capacidade, tipo) VALUES (%s, %s, %s) RETURNING id",
            (nome, capacidade, tipo)
        )
        conn.commit()
        return cursor.fetchone()[0]

    def update(self, id, nome, capacidade, tipo):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Atualizando galpão {id}.")
        cursor.execute(
            "UPDATE tb_galpao SET nome=%s, capacidade=%s, tipo=%s WHERE id=%s",
            (nome, capacidade, tipo, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Deletando galpão {id}.")
        cursor.execute("DELETE FROM tb_galpao WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
