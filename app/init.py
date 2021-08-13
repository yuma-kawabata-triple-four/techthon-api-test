from database.models import setup_db_table, insertInitialStock

if __name__ == "__main__":
    setup_db_table()
    insertInitialStock()
