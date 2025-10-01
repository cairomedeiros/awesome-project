from app.db.postgreSQL import connection_test

def get_db():
    db = connection_test()
    try:
        yield db
    finally:
        db.close()
