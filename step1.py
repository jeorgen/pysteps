# -*- coding: utf-8 -*-
import urllib

connection = urllib.urlopen('http://pythoncourse.webworks.se/eurovision')

result = connection.read()

print result

