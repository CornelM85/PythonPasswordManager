import sqlite3


class ConnectDB:

    def __init__(self):
        self.connection = sqlite3.connect('pswd_manager.db')

        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
            );          
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS websites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            login_name TEXT NOT NULL,
            login_password TEXT NOT NULL,
            url TEXT NOT NULL,
            url_name_displayed NOT NULL,
            image_name NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)   
            );
            """
        )

        self.connection.commit()
        # self.connection.close()

    def add_user(self, username, password, email):
        query = """
                INSERT INTO users (username, password, email)
                VALUES (?, ?, ?);
                """
        parameters = (username, password, email)
        self.cursor.execute(query, parameters)
        self.connection.commit()

    def add_website(self, user_id, login_name, login_password, url, url_name_displayed, image_name):
        query = """
                INSERT INTO websites (user_id, login_name, login_password, url, url_name_displayed, image_name)
                VALUES (?, ?, ?, ?, ?, ?);
                """
        parameters = (user_id, login_name, login_password, url, url_name_displayed, image_name)
        self.cursor.execute(query, parameters)
        self.connection.commit()

    def get_user_id(self, username, password):
        query = """
                SELECT id FROM users
                WHERE username = ? AND password = ?;
                """
        parameters = (username, password)

        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()[0]

    def check_credentials(self, username, password):
        query = """
                SELECT * FROM users
                WHERE username = ? AND password = ?;
                """
        parameters = (username, password)
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    def get_all_websites(self, user_id):
        query = """
                SELECT login_name, login_password, url_name_displayed, image_name FROM websites
                WHERE user_id = ?;
                """
        self.cursor.execute(query, user_id)
        return self.cursor.fetchall()

    def get_website(self, user_id, url_name_displayed):
        query = """
                SELECT url FROM websites
                WHERE user_id = ? and url_name_displayed = ?;
                """

        parameters = (user_id, url_name_displayed)
        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()[0]