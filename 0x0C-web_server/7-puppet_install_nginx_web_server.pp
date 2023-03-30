#mainfiest for nginx server
package { 'nginx':
  ensure => installed
}
file { '/var/www/html/index.nginx-debian.html':
    ensure  => present,
    content => 'Hello World!'
}
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @(END/L),
  server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;
      server_name _;
      location / {
              # First attempt to serve request as file, then
              # as directory, then fall back to displaying a 404.
              try_files $uri $uri/ =404;
      }
      location /redirect_me{
              return 301 https://www.facebook.com/sescozahmed/;
      }
  }
  | END
  notify  => Service['nginx']
}
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}
