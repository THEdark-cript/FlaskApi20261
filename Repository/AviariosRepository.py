from helpers.database import get_conn
from helpers.logger import logger
from models.Aviario import Aviario

class AviarioRepository:
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Buscando todos os aviários")
        cursor.execute("SELECT * FROM tb_aviarios")
        rows = cursor.fetchall()
        conn.close()
        return [Aviario(*row) for row in rows]

    def getById(self, id: int):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info(f"Buscando aviário pelo id {id}")
        cursor.execute("SELECT * FROM tb_aviarios WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Aviario(*row) if row else None

    def insert(self, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "INSERT INTO tb_aviarios (nome, localizacao, capacidade) VALUES (?, ?, ?)"
        cursor.execute(stmt, (dados["nome"], dados["localizacao"], dados["capacidade"]))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
        return id

    def update(self, id, dados):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "UPDATE tb_aviarios SET nome=?, localizacao=?, capacidade=? WHERE id=?"
        cursor.execute(stmt, (dados["nome"], dados["localizacao"], dados["capacidade"], id))
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        stmt = "DELETE FROM tb_aviarios WHERE id=?"
        cursor.execute(stmt, (id,))
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas
