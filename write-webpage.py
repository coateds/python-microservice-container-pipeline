#!/usr/bin/python
import time

htmlheader = "<html><head></head>"
htmlbodytop = "<body>"
htmlbodybottom = "</body></html>"

# htmlwhole = "<html><head></head><body>wholefile</body></html>"

count = 0

# This works (from append)
# while True:
#     index = open('/etc/nginx/html/index.html', 'a')
#     index.write('My new line<br>')
#     index.close
#     time.sleep(2)

# Write a whole static website out of concatenated
# string fragments, "count" needs to be converted to a string
# in this form, /etc/nginx/html/index.html needs to exist first
# copy an empty index.html file in the Dockerfile
while True:
    count += 1
    index = open('/etc/nginx/html/index.html', 'w')
    dynamicstring = htmlheader + htmlbodytop + "<p>dynamic line" + str(count) + "</p>" + htmlbodybottom
    index.write(dynamicstring)
    index.close
    time.sleep(2)    