# python-microservice-container-pipeline
A pipline for building a deploying a docker container with python and nginx. Launches a python script that periodically writes to the index.html file of nginx

## The pipeline
This pipeline is self contained in the jenkins-docker vagrant box. Use the PythonDevCen vagrant box browser to connect both to the nginx website output and the jenkins UI website.

## Goals
* Convert the python script to write html to the nginx website index.html
  * A string for the header
  * A string for the body top
  * Dynamic string with content
  * String with the body bottom
* Write a loop that performs a test
  * Simple Ping for now
* Write a function that converts a list to an html table row
* Work on ways to input a list (txt file) of servers/sites to ping
  * In the Dockerfile
  * File sharing with host

## Ancillary issues
Need to (fully) recover git to GitHub functionality. Adding a new file did not work from the client

Install (Windows) Python on laptop
