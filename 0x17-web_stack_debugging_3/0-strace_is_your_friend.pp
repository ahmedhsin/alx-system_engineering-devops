#fix using puppet
exec { 'debug2':
  command  => 'sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php;
  sudo service apache2 restart',
  provider => shell,
  path     => '/usr/bin',
}
