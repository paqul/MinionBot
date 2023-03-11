import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=RKCGVdqomRM&t=1302s&ab_channel=VietsubM%E1%BB%97iNg%C3%A0y',
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)
