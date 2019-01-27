import re
from bs4 import BeautifulSoup
import urllib
import ssl

def get_lyrics(artist, song):

    song = song.replace(' ', '')
    artist = artist.replace(' ', '')
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song+".html"

    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    lyrics = str(soup)

    # lyrics lies between up_partition and down_partition
    up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
    down_partition = '<!-- MxM banner -->'
    lyrics = lyrics.split(up_partition)[1]
    lyrics = lyrics.split(down_partition)[0]
    lyrics = lyrics.replace('<br>','')\
        .replace('</br>','')\
        .replace('</div>','')\
        .replace('<br/>','').strip()
    print(lyrics)
    f = open("songs/"+song+'.txt', "w+")
    f.write(lyrics)
    f.close()
    return lyrics


ssl._create_default_https_context = ssl._create_unverified_context
get_lyrics("kaleo", "save yourself")
get_lyrics("spice girls", "wannabe")
get_lyrics("drake", "one dance")
get_lyrics("kanye west", "gold digger")
get_lyrics("taio cruz", "dynamite")
get_lyrics("pitbull", "timber")
get_lyrics("justin bieber", "sorry")
get_lyrics("walk the moon", "shut up and dance")
get_lyrics("ed sheeran", "shape of you")