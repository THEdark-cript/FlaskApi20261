from helpers.database import get_conn
from helpers.logger import logger

class AvicolaRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Buscando todas as avícolas.")
        cursor.execute("SELECT * FROM tb_avicola")
        return cursor.fetchall()

    def getById(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Buscando avícola pelo id {id}.")
        cursor.execute("SELECT * FROM tb_avicola WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, endereco, territorio):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Repositório: Inserindo nova avícola.")
        cursor.execute(
            "INSERT INTO tb_avicola (endereco, territorio) VALUES (%s, %s) RETURNING id",
            (endereco, territorio)
        )
        conn.commit()
        return cursor.fetchone()[0]

    def update(self, id, endereco, territorio):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Atualizando avícola {id}.")
        cursor.execute(
            "UPDATE tb_avicola SET endereco=%s, territorio=%s WHERE id=%s",
            (endereco, territorio, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Repositório: Deletando avícola {id}.")
        cursor.execute("DELETE FROM tb_avicola WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount
