from sqlalchemy import create_engine

class DBConnection(object):

    def connection_test():
        engine = create_engine('postgresql+psycopg2://user:password@host:port/database-name')
        connection = engine.connect()
        print("Connected to PostgreSQL database successfully!")
        connection.close()