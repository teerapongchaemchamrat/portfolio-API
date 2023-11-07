from app.database import PgDatabase
from app.utils import verify_regular_expression
from app.error_variable import ERORR_PARAMETER


def insert_experince(skill_id, title, description, company):
    params = [skill_id, title, description, company]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = """INSERT INTO experince (skill_id, title, description, company)
                     VALUES (%s, %s, %s, %s);
                  """ % (skill_id, title, description, company)
            
            db.cursor.execute(sql)
            db.connection.commit()
            msg = "insert experince success..."
            return msg
    else:
        err = ERORR_PARAMETER
        return err

def select_experince():
    with PgDatabase() as db:
        sql = f"SELECT * FROM experince;"
        db.cursor.execute(sql)
        rows = db.cursor.fetchall()
        columns = [desc[0] for desc in db.cursor.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        if len(results) > 0:
            results = results[0]

        return results

# def select_experince(skill_id):
#     params = [skill_id]
#     if verify_regular_expression(params):
#         with PgDatabase() as db:
#             sql = f"SELECT * FROM experince WHERE skill_id = %s;" % skill_id
#             db.cursor.execute(sql)
#             rows = db.cursor.fetchall()
#             columns = [desc[0] for desc in db.cursor.description]
#             results = []
#             for row in rows:
#                 results.append(dict(zip(columns, row)))

#             if len(results) > 0:
#                 results = results[0]

#             return results
#     else:
#         err = ERORR_PARAMETER
#         return err


    
