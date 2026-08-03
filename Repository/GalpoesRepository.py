from helpers.database import get_conn
from helpers.logger import logger
from models.Galpao import Galpao

class GalpaoRepository:
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Buscando todos os galpões")
        cursor.execute("SELECT * FROM tb_galpoes")
        rows = cursor.fetchall()
        conn.close()
        return [Galpao(*row) for row in rows]

    def getById(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Buscando galpão pelo id {id}")
        cursor.execute("SELECT * FROM tb_galpoes WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Galpao(*row) if row else None

    def insert(self, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "INSERT INTO tb_galpoes (nome, capacidade, avicola_id) VALUES (?, ?, ?)"
        cursor.execute(stmt, (dados["nome"], dados["capacidade"], dados["avicola_id"]))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
        return id

    def update(self, id, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "UPDATE tb_galpoes SET nome=?, capacidade=?, avicola_id=? WHERE id=?"
        cursor.execute(stmt, (dados["nome"], dados["capacidade"], dados["avicola_id"], id))
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "DELETE FROM tb_galpoes WHERE id=?"
        cursor.execute(stmt, (id,))
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas
