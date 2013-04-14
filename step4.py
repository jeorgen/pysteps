# -*- coding: utf-8 -*-
# Adding exception handling for the fetching of data
# and putting some code in a function
import urllib
from datetime import datetime

url = 'http://pythoncourse.webworks.se/eurovision'

def handleresult(result):
    print result
    fo = open('moodtracker.log','a')
    now = datetime.now()
    now_as_string = str(now)
    fo.write(now_as_string + " " + result + "\n")
    fo.close()


try:
    connection = urllib.urlopen(url)
    result = connection.read()
    handleresult(result)
except IOError:
    print url, "did not work"





