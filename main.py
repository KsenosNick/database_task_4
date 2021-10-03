import sqlalchemy
from config import host, user, password, db_name, port

try:
    db = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()
    print('Successfully connected...')
    try:
        connection.execute("""
            SELECT title, year_issue FROM album 
            WHERE year_issue = 2018;
            """).fetchall()
        connection.execute("""
            SELECT title, duration FROM track 
            ORDER BY duration DESC
            LIMIT 1
            ;""").fetchone()
        connection.execute("""
            SELECT title, duration FROM track 
            WHERE duration > 210;
            """).fetchall()
        connection.execute("""
            SELECT title FROM collection 
            WHERE year_issue BETWEEN 2018 AND 2020;
            """).fetchall()
        connection.execute("""
            SELECT name FROM artist 
            WHERE name not like '%% %%';
            """).fetchall()
        connection.execute("""
            SELECT title FROM track 
            WHERE title ILIKE '%%my%%' OR title ILIKE '%%мой%%';
            """).fetchall()
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)


