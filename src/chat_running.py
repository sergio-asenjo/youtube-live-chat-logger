import pytchat
import emoji
from yt_live import getLive
from sql_queries import insert_chat, create_table

channelId = input("Enter Channel ID: ")
live_id, live_title = getLive(channelId)

chat = pytchat.create(video_id=live_id)
create_table()

while chat.is_alive():
    for c in chat.get().sync_items():
        msg_info = (c.author.channelId,
                    live_id,
                    live_title,
                    c.author.name,
                    c.author.isChatModerator,
                    c.datetime,
                    emoji.emojize(c.message))
        insert_chat(msg_info)
        print(emoji.emojize(f"{c.datetime} [{c.author.name}]- {c.message}"))