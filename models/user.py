from app.database import PgDatabase
from app.utils import verify_regular_expression
from app.error_variable import ERORR_PARAMETER

def read_user(username):
    params = [username]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""SELECT id, username, password FROM "users" WHERE username='{username}'; """
            db.cursor.execute(sql)
            rows = db.cursor.fetchall()
            columns = [desc[0] for desc in db.cursor.description]
            results = []
            for row in rows:
                results.append(dict(zip(columns, row)))
                
            if len(results) > 0:
                results = results[0]

            return results
    else:
        err = ERORR_PARAMETER
        return err
    
def read_all_user():
    with PgDatabase() as db:
        sql = f"""SELECT id FROM users;"""
        db.cursor.execute(sql)
        rows = db.cursor.fetchall()
        columns = [desc[0] for desc in db.cursor.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
            
        if len(results) > 0:
            results = results[0]

        return results
        
def add_user(username, password):
    params = [username]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""INSERT INTO "users" (username, password, created_date) VALUES ('{username}', '{password}', CURRENT_TIMESTAMP) returning id"""
            db.cursor.execute(sql)
            new_user_id = db.cursor.fetchone()[0] 
            db.connection.commit()
            return new_user_id
    else:
        err = ERORR_PARAMETER
        return err
