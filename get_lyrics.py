import re
from bs4 import BeautifulSoup
import urllib

def get_lyrics(artist, song):
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song+".html"
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    lyrics = str(soup)
    print(lyrics)
    # lyrics lies between up_partition and down_partition
    up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
    down_partition = '<!-- MxM banner -->'
    lyrics = lyrics.split(up_partition)[1]
    lyrics = lyrics.split(down_partition)[0]
    lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
    print(lyrics)
    f = open("songs/"+song, "w+")
    f.write(lyrics)
    f.close()
    return lyrics


get_lyrics("kaleo", "save yourself")