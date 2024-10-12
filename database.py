import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# Create a connection to the database


'''
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    for row in result:
        print(row)

'''


class database:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://egfwe479rau7ia8z:mgw5gfy1jf9qogm3@o677vxfi8ok6exrd.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/n8ic4928wg3p4wnn?charset=utf8mb4')

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