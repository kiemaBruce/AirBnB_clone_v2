#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static
# Check if Nginx is installed, only install if not install
if ! command -v nginx &> /dev/null
then
	# Install Nginx
	sudo apt-get update -q
	sudo apt-get install -qy nginx
fi
# Create directories if they don't exist
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
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
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html
# Create symbolic link
if [ -L /data/web_static/current ]
then
	rm /data/web_static/current
fi
ln --symbolic /data/web_static/releases/test /data/web_static/current
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
awk '/\tserver_name _;/ && !found {system("cat temp_file"); found=1; next} 1' /etc/nginx/sites-available/default > output_file
sudo rm temp_file
sudo mv output_file /etc/nginx/sites-available/default
#check for any errors with nginx config files
if sudo nginx -t
then
	# reload nginx
	sudo nginx -s reload
else
	echo "Error with nginx config files"
fi
