import sqlalchemy import create_engine
engine = create_engine('postgreesql://user:password@localhost/database_name')
connection = engine.connect()

result = connection.execute('SELECT * FROM table_name')
data = result.fetchall()

