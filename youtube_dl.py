from asyncio.format_helpers import extract_stack
import youtube_dl

video_url = input('link')
video_bilgisi = youtube_dl.YoutubeDL().extract_info(
url = video_url,download=False)
dosya_adi = f"{video_bilgisi['title']}.mp3"
ayarlar={
     'format':'bestauido/best',
     'keepvideo':False,
     'outtmpl':dosya_adi,
}

with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])


print('anan')


print(f"İndirme tamamlandı...{dosya_adi}")



