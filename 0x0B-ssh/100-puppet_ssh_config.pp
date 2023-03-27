#create config using puppet
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @(END/L),
Host ubunto
    HostName 54.209.141.133
    User ubuntu
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
| END
}
