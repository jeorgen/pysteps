# -*- coding: utf-8 -*-
# Adding file logging
import urllib

connection = urllib.urlopen('http://pythoncourse.webworks.se/eurovision')

result = connection.read()

print result

fo = open('moodtracker.log','a')
fo.write(result)
fo.close()
