# -*- coding: utf-8 -*-
# Using "with" syntax for file handling
import urllib
from datetime import datetime

url = 'http://admin.webworks.se/pythoncourse/eurovision'

def handleresult(result):
    print result
    with open('moodtracker.log','a') as fo:
        now = datetime.now()
        now_as_string = str(now)
        fo.write(now_as_string + " " + result + "\n")


try:
    connection = urllib.urlopen(url)
    result = connection.read()
    handleresult(result)
except IOError:
    print url, "did not work"





