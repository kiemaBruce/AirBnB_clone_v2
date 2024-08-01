#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static
# Check if Nginx is installed, only install if not install
if ! command -v nginx > /dev/null
then
	# Install Nginx
	sudo apt-get update > /dev/null
	sudo apt-get install -y nginx > /dev/null
fi
# Create directories if they don't exist
sudo mkdir /data/ > /dev/null 2>&1
sudo mkdir /data/web_static/ > /dev/null 2>&1
sudo mkdir /data/web_static/releases/ > /dev/null 2>&1
sudo mkdir /data/web_static/shared/ > /dev/null 2>&1
sudo mkdir /data/web_static/releases/test/ > /dev/null 2>&1
# Create simple html page
html_content=$(cat <<EOL
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOL
)
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null
# Create symbolic link
if [ -L /data/web_static/current ]
then
	sudo rm /data/web_static/current
fi
sudo ln --symbolic /data/web_static/releases/test /data/web_static/current > /dev/null
# Give ownership of a directory to a specific user and group
sudo chown -R ubuntu:ubuntu /data/
rep_str=$(cat <<EOL
        server_name _;

        location /hbnb_static {
               alias /data/web_static/current/; 
        }
EOL
)
echo "$rep_str" > temp_file
awk '/server_name _;/ && !found {system("cat temp_file"); found=1; next} 1' /etc/nginx/sites-available/default > output_file
sudo rm temp_file
sudo mv output_file /etc/nginx/sites-available/default
#check for any errors with nginx config files
if sudo nginx -t &> /dev/null
then
	# reload nginx
	sudo nginx -s reload
fi
