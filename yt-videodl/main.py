import yt_dlp as youtube_dl


def download_video(video_url, output_path='./downloads'):
    options = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', 'video')
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
