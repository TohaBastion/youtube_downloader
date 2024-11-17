import yt_dlp
from typing import Optional


def music_download(url: str, output_path: Optional[str] = None) -> None:
    """

    :param url: URL to download
    :param output_path: Optional path to save audio
    :return: None
    :raises Exceptions: If URL can't be downloaded
    """

    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Вибір найкращої якості аудіо
            'outtmpl': output_path + '\%(title)s.%(ext)s' if output_path else '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Формат файлу після конвертації
                'preferredquality': '192',  # Якість бітрейту (192 kbps)

            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('Sound downloaded')

    except Exception as e:
        print(f"error: {e}")


music_download('',
               output_path='')
