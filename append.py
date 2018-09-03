#!/usr/bin/python
import time

while True:
    index = open('/etc/nginx/html/index.html', 'a')
    index.write('My new line<br>')
    index.close
    time.sleep(2)
