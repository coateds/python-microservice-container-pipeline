#!/usr/bin/python
import time

htmlheader = "<html><head></head>"
htmlbodytop = "<body>"
htmlbodybottom = "</body></html>"

htmlwhole = "<html><head></head><body>wholefile</body></html>"

count = 0

# This works (from append)
# while True:
#     index = open('/etc/nginx/html/index.html', 'a')
#     index.write('My new line<br>')
#     index.close
#     time.sleep(2)

while True:
    count += 1
    index = open('/etc/nginx/html/index.html', 'W')
    # dynamicstring = htmlheader + htmlbodytop + "<p>dynamic line" + count + "</p>" + htmlbodybottom
    # index.write(dynamicstring)
    index.write(htmlwhole)
    index.close
    time.sleep(2)    