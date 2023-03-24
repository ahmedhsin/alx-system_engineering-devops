#execute a command
exec { 'kill a procces':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
