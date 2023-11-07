from app.database import PgDatabase
from app.utils import verify_regular_expression
from app.error_variable import ERORR_PARAMETER

def insert_portfolio(f_name, l_name, age, email, phone, line, address, education):
    params = [f_name, l_name, age, email, phone, line, address, education]
    if verify_regular_expression(params):
        with PgDatabase() as db:
            sql = f"""INSERT INTO portfolio (firstname, lastname, age, email, phonem, line, address, education)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """ % (f_name, l_name, age, email, phone, line, address, education)
            db.cursor.execute()
            db.connection.commit()
            msg = "insert portfolio success..."
            return msg
    else:
        err = ERORR_PARAMETER
        return err

def select_portfolio():
    with PgDatabase() as db:
        db.cursor.execute(f"SELETC * FROM portfolio;")
        rows = db.cursor.fetchall()
        columns = [desc[0] for desc in db.cursor.description]
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        if len(results) > 0 :
            results = results[0]
        return results