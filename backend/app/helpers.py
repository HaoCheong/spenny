from app.database.database import SessionLocal

# Gets an instance of the DB, will close connection with DB when done


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
