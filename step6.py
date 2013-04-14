# -*- coding: utf-8 -*-
# Making code into a module that can be called from other scripts
import urllib
from datetime import datetime


def _handleresult(result):
    print result
    now = datetime.now()
    now_as_string = str(now)
    with open('moodtracker.log','a') as fo:
        fo.write(now_as_string + " " + result + "\n")

def print_and_log_mood(url):
    try:
        connection = urllib.urlopen(url)
        result = connection.read()
        _handleresult(result)
    except IOError:
        print url, "did not work"
        
        
if __name__ == "__main__":
    url = 'http://pythoncourse.webworks.se/eurovision'
    print_and_log_mood(url)





