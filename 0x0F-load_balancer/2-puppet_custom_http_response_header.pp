exec { 'custom name':
  command  => 'sudo apt update -y;
	sudo apt install nginx -y;
	sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
	sudo service nginx sestart',
  provider => shell
}
