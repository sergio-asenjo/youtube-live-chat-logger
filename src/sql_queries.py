import sqlite3


connection = sqlite3.connect("chat.db")
c = connection.cursor()

def create_table():
    with connection:
        c.execute("""
                        CREATE TABLE IF NOT EXISTS chat (
                        channelId TEXT,
                        videoId TEXT NOT NULL,
                        videoTitle TEXT NOT NULL,
                        author TEXT NOT NULL,
                        isChatModerator BOOLEAN DEFAULT(FALSE),
                        datetime TEXT NOT NULL,
                        message TEXT NOT NULL
                    );
                    """)
        return connection.commit()

def insert_chat(msg_info):
    with connection:
        q = ("""INSERT INTO
                    chat(channelId,
                         videoId,
                         videoTitle,
                         author,
                         isChatModerator,
                         datetime,
                         message)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """)
        c.execute(q, msg_info)
        return connection.commit()