import os
import time
import json
import random
from googleapiclient.discovery import build
import yt_dlp

# Substitua pela sua chave de API do YouTube
API_KEY = ''

def get_channel_id(channel_handle):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    if channel_handle.startswith('@'):
        channel_handle = channel_handle[1:]

    request = youtube.search().list(
        q=channel_handle,
        part='snippet',
        type='channel',
        maxResults=1
    )
    response = request.execute()

    if response['items']:
        channel_id = response['items'][0]['snippet']['channelId']
        return channel_id
    else:
        raise Exception(f'Canal {channel_handle} não encontrado.')

def get_videos(channel_id, max_results=10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        channelId=channel_id,
        part='id,snippet',
        maxResults=30,
        type='video',
        videoDuration='medium'
    )
    response = request.execute()

    video_data = [{'videoId': item['id']['videoId'], 'title': item['snippet']['title']} for item in response['items']]
    return [video['videoId'] for video in video_data[:max_results]]
    
def get_short_videos(channel_id, max_results=10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        channelId=channel_id,
        part='id',
        maxResults=max_results,
        type='video',
        videoDuration='short'
    )
    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]
    return video_ids

def download_video(video_id, download_path):
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    print(f'Tentando baixar o vídeo: {video_url}')
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            print(f'Vídeo {video_url} baixado com sucesso!')
            return info_dict['id']  # Retorna o ID do vídeo baixado
    except Exception as e:
        print(f'Erro ao baixar o vídeo {video_url}: {e}')
        return None

def load_downloaded_ids(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Arquivo JSON malformado: {file_path}. Retornando lista vazia.")
            return []
    return []

def save_downloaded_ids(file_path, video_ids):
    with open(file_path, 'w') as f:
        json.dump(video_ids, f)

def get_random_channel(channels):
    return random.choice(channels)

def main():
    channels = [
        "@cortesdointeligencia",
        "@CortesPodpahOFICIAL",
        "@cortesdoflow"
    ]
    
    channel_handle = get_random_channel(channels)
    num_videos = 20
    download_path = 'downloads'
    json_file_path = 'downloaded_videos.json'
    
    os.makedirs(download_path, exist_ok=True)
    
    try:
        channel_id = get_channel_id(channel_handle) if not channel_handle.startswith('UC') else channel_handle
        print(f'ID do Canal encontrado: {channel_id}')
        
        downloaded_ids = load_downloaded_ids(json_file_path)
        video_ids = get_videos(channel_id, max_results=num_videos)

        for video_id in video_ids:
            if video_id not in downloaded_ids:
                result = download_video(video_id, download_path)
                if result:
                    downloaded_ids.append(result)
                    time.sleep(5) 
            else:
                print(f'O vídeo {video_id} já foi baixado. Pulando...')
        
        save_downloaded_ids(json_file_path, downloaded_ids)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
