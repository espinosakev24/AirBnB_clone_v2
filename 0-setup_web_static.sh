#!/usr/bin/env bash
apt-get install nginx
mkdir -p data/web_static/releases/test && touch data/web_static/releases/test/index.html
mkdir data/web_static/shared
if [ -L data/web_static/current ]
then
    rm data/web_static/current
    ln -s data/web_static/current
else
    ln -s data/web_static/current
fi
chown --recursive ubuntu:ubuntu /data
sed -i "s/^[\t]location \/ {$/location \/hbnb_static {\n\talias \/data\/web_static\/current\/\n\tautoindex off/g;" /etc/nginx/sites-available/default
sudo service nginx restart
