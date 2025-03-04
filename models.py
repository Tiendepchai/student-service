from database import get_db_connection

def create_student_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_db (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            age INT NOT NULL,
            major VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    conn.close()
