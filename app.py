import psycopg2

def main():
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="db"
    )
    cur = conn.cursor()

    # Создание таблицы
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            department VARCHAR(100)
        )
    """)

    # Наполнение таблицы данными
    cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Alice", 30, "HR"))
    cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Bob", 40, "Engineering"))
    cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Charlie", 35, "Sales"))

    # Вывод данных из таблицы
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    # Закрытие соединения
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
