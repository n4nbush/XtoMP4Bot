import yt_dlp

def descargar_video(url):
    opciones = {
        'outtmpl': 'video.mp4',  # Nombre del archivo
    }
    
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])
    
    return 'video.mp4'

