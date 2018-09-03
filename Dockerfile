# comments in a Dockerfile?

# Base image
FROM yobasystems/alpine-nginx:latest

# Set up working directory and copy files to it from GitHub
ENV DIRPATH /opt/dcoate-app/
WORKDIR $DIRPATH
ADD write-webpage.py $DIRPATH
#ADD append.py $DIRPATH
ADD mycmd.sh $DIRPATH

# Copy a new web index.html page from GitHub
ADD index.html /etc/nginx/html/index.html

# Install bash and python
RUN apk add --no-cache bash python2-dev python2 py2-pip

# run the bash script in the 2nd parameter
# this script will run a python script in the background and then launch nginx
CMD ["/bin/bash", "mycmd.sh"]