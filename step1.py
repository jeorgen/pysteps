# -*- coding: utf-8 -*-
import urllib

connection = urllib.urlopen('http://admin.webworks.se/pythoncourse/eurovision')

result = connection.read()

print result

