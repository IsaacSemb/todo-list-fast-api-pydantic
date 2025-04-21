from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

database_url_format = '<dialect>+<driver>://<username>:<password>@<host>:<port(optional)>/<database_name>'

notes = """

the dialect is the server of SQL
whose sql are you using 
who created the interface to this specific sql that youre using

Examples include
- mysql
- postgres
- oracle
- sqlite

"""

# using python sql connector
# DATABASE_URL2 = "mysql+mysqlconnector://root:1234@localhost/todo_api"

# using pymysql
#  manual creation
DATABASE_URL1 = "mysql+pymysql://root:1234@localhost/todo_api"

# auto creation if you want to avoid mistakes -- also it hides the password
DATABASE_URL2 = URL.create(
    drivername='mysql+pymysql',
    username='root',
    password='1234',
    host='localhost',
    database='todo_api'
)

db_engine = create_engine(DATABASE_URL1)

session = sessionmaker(
    bind=db_engine,
    autocommit=False, # meaning the dev calls the commit rather than auto ( good habit )
    autoflush=False
)

Base  = declarative_base()

