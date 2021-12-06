import os
from googleapiclient.discovery import build

yt = build('youtube', 'v3', developerKey=os.environ.get("YOUTUBE_KEY"))

def getLive(channel_id):

    live_request = yt.search().list(
        part='snippet',
        channelId=channel_id,
        eventType='live',
        type='video'
    )

    response = live_request.execute()

    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        return video_id, video_title