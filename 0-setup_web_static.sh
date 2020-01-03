#!/usr/bin/env bash
# Creating files and setting up the nginx file 
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test && touch /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared
echo "holbertonschool" > /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]
then
    rm /data/web_static/current
    ln -snf /data/web_static/releases/test /data/web_static/current
else
    ln -snf /data/web_static/releases/test /data/web_static/current
fi
chown --recursive ubuntu:ubuntu /data
sed -i "60i location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
