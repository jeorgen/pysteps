# -*- coding: utf-8 -*-
# Making our Eurovision mood report into a web server
import urllib
from datetime import datetime
from bottle import route, run

def _logresult(result):
    now = datetime.now()
    now_as_string = str(now)
    with open('moodtracker.log','a') as fo:
        fo.write(now_as_string + " " + result + "\n")

@route('/')
def show_and_log_mood():
    url = 'http://pythoncourse.webworks.se/eurovision'
    try:
        connection = urllib.urlopen(url)
        result = connection.read()
    except IOError:
        result =  url + "fetch did not work"
    _logresult(result)
    return "Mood is: " + result
     
if __name__ == '__main__':
    run(host='0.0.0.0', port=58080)
    
# Your job: make this script use the code in previous step






