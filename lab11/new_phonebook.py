import psycopg2
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

    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print("Table created.\n")


def init_db():
    commands = [
        """
        CREATE OR REPLACE PROCEDURE pr_add_user(
            IN p_username TEXT,
            IN p_phone    TEXT
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
                UPDATE phonebook
                SET phone = p_phone
                WHERE username = p_username;
            ELSE
                INSERT INTO phonebook(username, phone)
                VALUES (p_username, p_phone);
            END IF;
        END;
        $$;
        """,
        """
        CREATE OR REPLACE PROCEDURE pr_add_users(
            IN  p_usernames TEXT[],
            IN  p_phones    TEXT[],
            OUT bad_usernames TEXT[],
            OUT bad_phones    TEXT[]
        )
        LANGUAGE plpgsql
        AS $$
        DECLARE
            i INT;
        BEGIN
            bad_usernames := ARRAY[]::TEXT[];
            bad_phones    := ARRAY[]::TEXT[];

            IF array_length(p_usernames, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
                RAISE EXCEPTION 'Arrays must have the same length';
            END IF;

            FOR i IN 1..COALESCE(array_length(p_usernames, 1), 0) LOOP
                IF length(p_phones[i]) BETWEEN 10 AND 15 THEN
                    CALL pr_add_user(p_usernames[i], p_phones[i]);
                ELSE
                    bad_usernames := bad_usernames || p_usernames[i];
                    bad_phones    := bad_phones    || p_phones[i];
                END IF;
            END LOOP;
        END;
        $$;
        """,
        """

        CREATE OR REPLACE FUNCTION fn_get_page(
            p_limit  INT,
            p_offset INT
        )
        RETURNS SETOF phonebook
        LANGUAGE sql
        AS $$
            SELECT *
            FROM phonebook
            ORDER BY id
            LIMIT p_limit
            OFFSET p_offset;
        $$;
        """,
        """
        CREATE OR REPLACE PROCEDURE pr_del_user(
            IN p_username TEXT,
            IN p_phone    TEXT
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM phonebook
            WHERE (p_username IS NOT NULL AND username = p_username)
               OR (p_phone    IS NOT NULL AND phone    = p_phone);
        END;
        $$;
        """
    ]

    conn = connect()
    cur = conn.cursor()
    for cmd in commands:
        cur.execute(cmd)
    conn.commit()
    cur.close()
    conn.close()
    print("Procedures and function created.\n")


def ins_one():
    name = input("Enter username: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL pr_add_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("User inserted/updated.\n")


def ins_many():
    try:
        n = int(input("How many users? "))
    except ValueError:
        print("Need a number.\n")
        return

    names = []
    phones = []

    for i in range(n):
        print("User", i + 1)
        name = input("  Username: ")
        phone = input("  Phone: ")
        names.append(name)
        phones.append(phone)

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL pr_add_users(%s, %s, %s, %s);",
        (names, phones, None, None)
)
    bad_usernames, bad_phones = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    print("\nDone.")
    if bad_usernames:
        print("Incorrect phones:")
        for u, p in zip(bad_usernames, bad_phones):
            print("  name =", u, "phone =", p)
        print()
    else:
        print("All phones are correct.\n")


def show_page():
    try:
        limit = int(input("LIMIT: "))
        offset = int(input("OFFSET: "))
    except ValueError:
        print("Need numbers.\n")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fn_get_page(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if rows:
        print("\nRows:")
        for row in rows:
            print(row)
        print()
    else:
        print("No rows on this page.\n")


def del_user():
    name = input("Username to delete (or empty): ")
    phone = input("Phone to delete (or empty): ")

    if name.strip() == "":
        name = None
    if phone.strip() == "":
        phone = None

    if name is None and phone is None:
        print("Nothing to delete.\n")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL pr_del_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Delete done.\n")


def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Create table")
        print("2 - Init DB")
        print("3 - Insert/Update one user")
        print("4 - Insert many users")
        print("5 - Show page")
        print("6 - Delete user")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            init_db()
        elif choice == "3":
            ins_one()
        elif choice == "4":
            ins_many()
        elif choice == "5":
            show_page()
        elif choice == "6":
            del_user()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    menu()