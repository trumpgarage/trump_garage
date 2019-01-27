from numpy.random import choice
import probability
import os
import crawler


def load_file(fp):

    text = 'START \n'
    with open(fp, "r") as f:
        for line in f:
            l = line.strip('\n()')
            text = text + l + ' \n '
    text = text + 'END'
    return text

def build_input(nextwords, text):
    text = text.replace('(', '')
    text = text.replace(')', '')
    words = text.split(' ')

    for i in range(len(words)):
        curr = words[i]
        if curr != "END":
            nxt = words[i+1]
            nextwords = update_dict(nextwords, curr, nxt)

    return nextwords


def update_dict(nextwords, curr, nxt):

    if curr in nextwords:
        if nxt in nextwords[curr]:
            nextwords[curr][nxt] += 1
        else:
            nextwords[curr][nxt] = 1
    else:
        nextwords[curr] = {nxt:1}
    return nextwords

def make_song():
    song = ''
    dirlist = os.listdir('songs/')
    nextwords={}

    for i in range(len(dirlist)):
        text = load_file('songs/'+ dirlist[i])
        nextwords = build_input(nextwords,text)

    nxt = 'START'
    while nxt != 'END':
        probs = probability.get_percentages(list(nextwords[nxt].values()))
        nxt = choice(list(nextwords[nxt]), p=probs)
        song = song + ' ' + nxt

    return song

def make_tweet(hashtag="#Brexit", language="en"):
    twet = ''
    nextwords = {}

    for t in crawler.get_tweets(hashtag, language):
        nextwords = build_input(nextwords, t)

    nxt = 'START'
    while nxt != 'END':
        probs = probability.get_percentages(list(nextwords[nxt].values()))
        nxt = choice(list(nextwords[nxt]), p=probs)
        twet = twet + ' ' + nxt

    return twet


if __name__ == '__main__':
    #print(make_song())
    #print(make_tweet('#KaarisvsBooba', "fr"))
    #print(make_tweet('#KaarisvsBooba', "fr"))
    #print(make_tweet('#KaarisvsBooba', "fr"))

    print(make_tweet('#brexit', "en"))
    print(make_tweet('#brexit', "en"))
    print(make_tweet('#brexit', "en"))



