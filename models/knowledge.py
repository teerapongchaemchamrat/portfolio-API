from app.database import PgDatabase
from app.utils import verify_regular_expression
from app.error_variable import ERORR_PARAMETER


def insert_knowledge(skill_id, title, description):
    params = [skill_id, title, description]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""INSERT INTO knowledge (skill_id, title, description, created_date)
                      VALUES (%s, %s, %s, CURRENT_TIMESTAMP);
                  """ % (skill_id, title, description)
            db.cursor.execute(sql)
            db.connection.commit()
            msg = "insert knowledge success..."
            return msg
    else:
        err = ERORR_PARAMETER
        return err

def select_knowledge():
    with PgDatabase() as db:
        db.cursor.execute(f"SELETC * FROM knowledge;")
        rows = db.cursor.fetchall()
        columns = [desc[0] for desc in db.cursor.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
        if len(results) > 0:
            results = results[0]
        return results
    
def update_knowledge(skill_id, title, description):
    params = [skill_id, title, description]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""UPDATE knowledge 
                      SET title = %s, description = %s, update_date = CURRENT_TIMESTAMP
                      WHERE skill_id = %s;
                   """ % (title, description, skill_id)
            db.cursor.execute()
            db.connection.commit()
            msg = "update knowledge success..."
            return msg
    else:
        err = ERORR_PARAMETER
        return err


def delete_knowledge(skill_id):
    params = [skill_id]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            db.cursor.execute(f"""DELETE FROM knowledge WHERE skill_id = %s;""" % (skill_id))
            db.connection.commit()
            msg = "delete knowledge success..."
            return msg 
    else:
        err = ERORR_PARAMETER
        return err