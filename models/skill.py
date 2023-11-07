from app.database import PgDatabase
from app.utils import verify_regular_expression
from app.error_variable import ERORR_PARAMETER

def select_skill():
    with PgDatabase() as db:
        db.cursor.execute(f"SELETC * FROM skill;")
        rows = db.cursor.fetchall()
        columns = [desc[0] for desc in db.cursor.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        if len(results) > 0:
            results = results[0]
        return results


def insert_skill(skill_id, dept, tools_name, language):
    params = [skill_id, dept, tools_name, language]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""INSERT INTO skill (skill_id, department, tools_name, programming_language)
                      VALUES (%s, %s, %s, %s);
                   """ % (skill_id, dept, tools_name, language)
            db.cursor.execute(sql)
            db.connection.commit()
            msg = "insert skill success..."
            return msg

    else: 
        err = ERORR_PARAMETER
        return err


def update_skill(skill_id, dept, tools_name, language):
    params = [skill_id, dept, tools_name, language]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""UPDATE skill (skill_id, department, tools_name, programming_language)
                      VALUES (%s, %s, %s, %s);
                 """ % (skill_id, dept, tools_name, language)
            db.cursor.execute(sql)
            db.connection.commit()
            msg = "update skill success..."
            return msg 
    else:
        err = ERORR_PARAMETER
        return err
