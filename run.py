#  -*- coding: utf-8 -*-


import feedparser
import sys


newsfeeds = ['https://www.reddit.com/r/worldnews/.rss']
def readdata():
    for n in newsfeeds:
       feeds = feedparser.parse(n)
       print("###### %s ######" % n)
       for feed in feeds.entries:
           print(feed.title + " " + feed.link + '\n')
    promt = input("")
    if promt == '1':
        readdata()

if __name__ == "__main__":
    readdata()