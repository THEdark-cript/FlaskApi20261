import sqlite3

DATABASE_NAME = "avicola.db"

def get_conn():
  # Cria uma conexão com o banco de dados SQLite
  conn = sqlite3.connect(DATABASE_NAME)
  return conn