# Import necessary library
import googleapiclient.discovery

# API information
api_service = "youtube"
api_version = "v3"
api_key = <API KEY> #API KEY censored

def last_n_video_channel(n,channel_id):
    #API Client
    youtube = googleapiclient.discovery.build(
        api_service, api_version, developerKey = api_key
    )

    #Querying upload playlist id from the channel
    request_channel = youtube.channels().list(
        part = "contentDetails",
        id = channel_id,
        maxResults=1
    )
    response_channel = request_channel.execute()
    upload_playlist_id = response_channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    #Querying video_id of last 100 videos in the channel
    request_playlist = youtube.playlistItems().list(
        playlistId = upload_playlist_id,
        part = "snippet",
        maxResults = n
    )
    response_playlist = request_playlist.execute()
    video_id_list = [video['snippet']['resourceId']['videoId'] for video in response_playlist["items"]]


    #Querying videos detail
    videos_response = youtube.videos().list(
        id=','.join(video_id_list),
        part="snippet,statistics,contentDetails,status"
    ).execute()

    videos_list=[]
    for video in videos_response['items']:
        row={
            "_id" : video["id"],
            "title" : video['snippet']['title'],
            "description" : video['snippet'].get('description', ""),
            "duration"  :  video['contentDetails']['duration'],
            "definition"  :  video['contentDetails']['definition'],
            "publishedAt" : video["snippet"]["publishedAt"],
            "madeForKids" : video["status"].get('madeForKids', False),
            "category_id"   :   video["snippet"].get("categoryId", ""),
            "tags" : video["snippet"].get("tags", ""),
            "views" : video['statistics']['viewCount']
        }
        videos_list.append(row)
    return videos_list
