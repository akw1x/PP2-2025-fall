import psycopg2
from config import load_config

def connect():
    params = load_config()
    return psycopg2.connect(**params)


def create_tables():
    sql_user = """
    CREATE TABLE IF NOT EXISTS game_user (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """

    sql_score = """
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES game_user(id),
        level INTEGER DEFAULT 1,
        score INTEGER DEFAULT 0
    );
    """

    conn = connect()
    cur = conn.cursor()
    cur.execute(sql_user)
    cur.execute(sql_score)
    conn.commit()
    cur.close()
    conn.close()


def get_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


def create_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
                (user_id, 1, 0))
    conn.commit()
    cur.close()
    conn.close()
    return user_id


def get_user_score(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data


def save_progress(user_id, level, score):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE user_score SET level = %s, score = %s WHERE user_id = %s",
        (level, score, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()


def login_user():
    username = input("Enter your username: ")
    user = get_user(username)

    if user is None:
        print("New player! Profile created.")
        user_id = create_user(username)
        return user_id, 1, 0
    else:
        user_id = user[0]
        level, score = get_user_score(user_id)
        print(f"Welcome back, {username}!")
        print(f"Your level: {level}, score: {score}")
        return user_id, level, score


if __name__ == "__main__":
    create_tables()
    user_id, level, score = login_user()
    level += 1
    score += 10
    save_progress(user_id, level, score)
    