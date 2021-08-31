dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogdb'}
import mysql.connector

print(dbconfig)

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()
# _SQL = """show tables"""
_SQL = """describe log"""

cursor.execute(_SQL)

res = cursor.fetchall()


