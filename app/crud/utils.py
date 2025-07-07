

# WARNING: TESTING ONLY - DO NOT USE IN PRODUCTION ROUTES
def create_all_tables(engine):
   """
   Creates all tables defined in the SQLAlchemy metadata using the provided engine.

   Args:
      engine: SQLAlchemy engine bound to the target database.

   Notes:
      This operation is database-destructive if followed by `drop_all_tables`. 
      Should only be used for initialization or testing purposes.
   """
   database.Base.metadata.create_all(bind=engine)
   
def drop_all_tables(engine):
   """
   Drops all tables defined in the SQLAlchemy metadata using the provided engine.

   Args:
      engine: SQLAlchemy engine bound to the target database.

   Warning:
      This operation is irreversible and will delete all data and schema definitions. 
      For testing or development use only.
   """
   database.Base.metadata.drop_all(bind=engine)

def reset_database(engine):
   """
   Completely resets the database by dropping and recreating all tables.

   Args:
      engine: SQLAlchemy engine bound to the target database.

   Warning:
      This function destroys all data and schema. Use it strictly in non-production environments 
      such as testing or local development.
   """
   
   drop_all_tables(engine)
   create_all_tables(engine)

# Drop and recreate any table
def reset_table(engine, table):
   """
   Resets a specific table by dropping and recreating it.

   Args:
      engine: SQLAlchemy engine bound to the target database.
      table: SQLAlchemy model class representing the table to be reset.

   Notes:
      Useful for isolated testing or when modifying a specific table's schema during development.
      Existing data in the table will be lost.
   """
   table.__table__.drop(bind=engine, checkfirst=True)
   table.__table__.create(bind=engine, checkfirst=True)

