from app.database import PgDatabase

def create_users():
    with PgDatabase() as db:
        db.cursor.execute("""
            CREATE TABLE "users" (
                id              SERIAL          PRIMARY KEY,
                username        VARCHAR(50)     NOT NULL,
                password        VARCHAR(255)    NOT NULL,
                created_date    TIMESTAMPTZ,
                updated_date    TIMESTAMPTZ,
                deleted_date    TIMESTAMPTZ
            )
        """)
        db.connection.commit()
        print("table user are created successfully...")


def drop_tables():
    with PgDatabase() as db:
        db.cursor.execute(f"""DROP TABLE IF EXISTS "users" CASCADE;""")
        db.connection.commit()
        print("Tables are dropped...")

def create_tables_portfolio():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE IF NOT EXISTS portfolio (
            firstname VARCHAR(50),
            lastname VARCHAR(50),
            age INTEGER,
            email VARCHAR(50),
            phone INTEGER,
            line VARCHAR(50),
            address VARCHAR(200),
            education VARCHAR(100),              
            created_date TIMESTAMPTZ DEFAULT NOW()
            );
        """)
        db.connection.commit()
        print("Table portfolio is created successfully...")

def create_tables_experince():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE IF NOT EXISTS experince (
            skill_id SERIAL INTEGER,
            title VARCHAR(100),
            description VARCHAR(500),
            company VARCHAR(500),
            create_date TIMESTAMPTZ DEFAULT NOW(),
            update_date TIMESTAMPTZ DEFAULT NOW(),
            delete_date TIMESTAMPTZ DEFAULT NOW(),
            CONSTRAINT experince_pkey PRIMARY KEY (skill_id)    
            );
        """)
        db.connection.commit()
        print("Table experince is created successfully...")

def create_tables_skill():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE IF NOT EXISTS skill (
            skill_id SERIAL INTEGER,
            department VARCHAR(50),
            tools_name VARCHAR(50),
            programming_language VARCHAR(100),
            create_date TIMESTAMPTZ DEFAULT NOW(),
            update_date TIMESTAMPTZ DEFAULT NOW(),
            delete_date TIMESTAMPTZ DEFAULT NOW(),
            CONSTRAINT skill_pkey PRIMARY KEY (skill_id)        
            );
        """)
        db.connection.commit()
        print("Table skill is created successfully...")

def create_tables_knowledge():
    with PgDatabase() as db:
        db.cursor.execute(f"""CREATE TABLE IF NOT EXISTS knowledge (
            skill_id SERIAL  INTEGER,
            title VARCHAR(50),
            description VARCHAR(50),
            create_date TIMESTAMPTZ DEFAULT NOW(),
            update_date TIMESTAMPTZ DEFAULT NOW(),
            delete_date TIMESTAMPTZ DEFAULT NOW(),
            CONSTRAINT knowledge_pkey PRIMARY KEY (skill_id)      
            );
        """)
        db.connection.commit()
        print("Table knowledge is created successfully...")
