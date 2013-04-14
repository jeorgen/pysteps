# -*- coding: utf-8 -*-
# Adding time stamps in the log
import urllib
from datetime import datetime

connection = urllib.urlopen('http://admin.webworks.se/pythoncourse/eurovision')

result = connection.read()

print result

fo = open('moodtracker.log','a')
now = datetime.now()
now_as_string = str(now)
fo.write(now_as_string + " " + result + "\n")
fo.close()
