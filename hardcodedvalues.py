
###########  Define hard coded variables  ###########

oses = { 'debian': { 'installer': 'apt', 'vagrantbox': 'debian/jessie64', 'vagrantbox_url': 'https://atlas.hashicorp.com/debian/boxes/jessie64' },
        'ubuntu': { 'installer': 'apt', 'vagrantbox': 'ubuntu/trusty64', 'vagrantbox_url': 'https://atlas.hashicorp.com/ubuntu/boxes/trusty64'},
         'redhat': { 'installer': 'yum', 'vagrantbox': '', 'vagrantbox_url': ''},
         'centos6': { 'installer': 'yum', 'vagrantbox': 'centos/6', 'vagrantbox_url': 'https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box'},
         'centos7': { 'installer': 'yum', 'vagrantbox': 'centos/7', 'vagrantbox_url': 'https://atlas.hashicorp.com/centos/boxes/7'},
         'freebsd': { 'installer': 'yum', 'vagrantbox': 'freebsd/FreeBSD-10.2-STABLE', 'vagrantbox_url': ''},
}
