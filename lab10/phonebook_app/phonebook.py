import psycopg2
import csv
from config import load_config


def connect():
    params = load_config()
    return psycopg2.connect(**params)


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print("Table created successfully!\n")
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")

    sql = "INSERT INTO phonebook(username, phone) VALUES (%s, %s);"

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (username, phone))
        conn.commit()
        cur.close()
        print("Inserted successfully!\n")
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_from_csv():
    filename = input("Enter CSV filename (example: phonebook.csv): ")

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()

        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook(username, phone) VALUES (%s, %s)",
                    (row["username"], row["phone"])
                )

        conn.commit()
        cur.close()
        print("CSV data inserted!\n")
    except FileNotFoundError:
        print("File not found!")
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_user():
    username = input("Enter username to update: ")
    new_phone = input("Enter new phone number: ")

    sql = "UPDATE phonebook SET phone = %s WHERE username = %s;"

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (new_phone, username))
        conn.commit()
        cur.close()
        print("Updated successfully!\n")
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def query_users():
    keyword = input("Enter part of name to search: ")

    sql = "SELECT * FROM phonebook WHERE username ILIKE %s;"

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (f"%{keyword}%",))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
            print()
        else:
            print("No users found!\n")
        cur.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_user():
    username = input("Enter username to delete: ")

    sql = "DELETE FROM phonebook WHERE username = %s;"

    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (username,))
        conn.commit()
        cur.close()
        print("Deleted successfully!\n")
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Create table")
        print("2 - Insert (console)")
        print("3 - Insert (CSV)")
        print("4 - Update")
        print("5 - Query")
        print("6 - Delete")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            insert_from_csv()
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_users()
        elif choice == "6":
            delete_user()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    menu()