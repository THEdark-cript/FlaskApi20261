from helpers.database import get_conn
from helpers.logger import logger

class AvicolaRepository():
    def getByIdAvicola(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando statement Avícola.")
        stmt = "SELECT * FROM tb_avicolas WHERE id=?"
        cursor.execute(stmt, (id,))
        row = cursor.fetchone()
        return row

    def getAllAvicolas(self):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "SELECT * FROM tb_avicolas"
        cursor.execute(stmt)
        rows = cursor.fetchall()
        return rows

    def insertAvicola(self, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "INSERT INTO tb_avicolas (nome, tipo, capacidade) VALUES (?, ?, ?)"
        cursor.execute(stmt, (dados["nome"], dados["tipo"], dados["capacidade"]))
        conn.commit()
        id = cursor.lastrowid
        return id

    def updateAvicola(self, id, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "UPDATE tb_avicolas SET nome=?, tipo=?, capacidade=? WHERE id=?"
        cursor.execute(stmt, (dados["nome"], dados["tipo"], dados["capacidade"], id))
        conn.commit()
        return cursor.rowcount

    def deleteAvicola(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "DELETE FROM tb_avicolas WHERE id=?"
        cursor.execute(stmt, (id,))
        conn.commit()
        return cursor.rowcount
