import sqlite3

connection = sqlite3.connect("chat.sqlite")
cursor = connection.cursor()

def create_table():
    with connection:
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS chat (
                        channelId TEXT,
                        videoId TEXT NOT NULL,
                        videoTitle TEXT NOT NULL,
                        author TEXT NOT NULL,
                        isChatModerator INTEGER DEFAULT(0),
                        datetime TEXT NOT NULL,
                        message TEXT NOT NULL
                    );
                    """)
        return connection.commit()

def insert_chat(msg_info):
    with connection:
        query = ("""INSERT INTO
                    chat(channelId,
                         videoId,
                         videoTitle,
                         author,
                         isChatModerator,
                         datetime,
                         message)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """)
        cursor.execute(query, msg_info)
        return connection.commit()