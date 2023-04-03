import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def get_channel_videos(channel_id, api_key):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Get the channel's uploads playlist ID
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Get the videos in the uploads playlist
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=uploads_playlist_id,
            pageToken=next_page_token
        )
        response = request.execute()
        videos.extend(response["items"])
        next_page_token = response.get("nextPageToken")

        if next_page_token is None:
            break

    return videos


def main():
    api_key = "YOUR_API_KEY"  # Replace with your API key
    channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Replace with the channel ID you want to get the videos from

    videos = get_channel_videos(channel_id, api_key)

    print("List of video titles:")
    for video in videos:
        print(video["snippet"]["title"])


if __name__ == "__main__":
    main()
