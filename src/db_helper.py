from config import db, app
from sqlalchemy import text

def table_exists():
  sql_table_existence = text(
    "SELECT EXISTS ("
    "  SELECT 1"
    "  FROM information_schema.tables"
    f" WHERE table_name = 'todos'"
    ")"
  )

  print(f"Checking if table todos exists")
  print(sql_table_existence)

  result = db.session.execute(sql_table_existence)
  return result.fetchall()[0][0]

def reset_db():
  print(f"Clearing contents from table todos")
  sql = text(f"DELETE FROM todos")
  db.session.execute(sql)
  db.session.commit()

def setup_db():
  if table_exists():
    print(f"Table todos exists, dropping")
    sql = text(f"DROP TABLE todos")
    db.session.execute(sql)
    db.session.commit()

  print(f"Creating table")
  
  # Read schema from schema.sql file
  import os
  schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
  with open(schema_path, 'r') as f:
    schema_sql = f.read().strip()
  
  sql = text(schema_sql)
  db.session.execute(sql)
  db.session.commit()

if __name__ == "__main__":
    with app.app_context():
      setup_db()
