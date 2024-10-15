import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine, text

load_dotenv()

# Create a connection to the database
class database:
    def __init__(self):
        # Read the connection string components from the .env file
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        dbname = os.getenv('DB_NAME')

        # Format the connection string
        connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'
        
        # Create the engine using the connection string
        self.engine = create_engine(connection_string)
        

    def print_jobs(self):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM jobs"))
            print(type(result))
            print(result)
            for row in result:
                print(type(row))
                print(row)
                print(row[0], row[1], row[2], row[3])
    
    def load_jobs_dicts_from_db(self):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM jobs"))
            jobs = []
            for row in result:
                job_dic = { 'id': row[0], 'title': row[1], 'location': row[2], 'salary': row[3] }
                jobs.append(job_dic)
            return jobs

db1 = database()

jobs = db1.load_jobs_dicts_from_db()
print(jobs)