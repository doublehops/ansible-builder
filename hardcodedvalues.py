
###########  Define hard coded variables  ###########

oses = { 'debian': { 'installer': 'apt', 'vagrantbox': 'debian/jessie64', 'vagrantbox_url': 'https://atlas.hashicorp.com/debian/boxes/jessie64' },
         'ubuntu': { 'installer': 'apt', 'vagrantbox': 'ubuntu/trusty64', 'vagrantbox_url': 'https://atlas.hashicorp.com/ubuntu/boxes/trusty64'},
         'redhat': { 'installer': 'yum', 'vagrantbox': '', 'vagrantbox_url': ''},
         'centos6': { 'installer': 'yum', 'vagrantbox': 'bento/centos-6.7', 'vagrantbox_url': 'https://atlas.hashicorp.com/bento/boxes/centos-6.7'},
         'centos7': { 'installer': 'yum', 'vagrantbox': 'centos/7', 'vagrantbox_url': 'https://atlas.hashicorp.com/centos/boxes/7'},
         'freebsd': { 'installer': 'yum', 'vagrantbox': 'freebsd/FreeBSD-10.2-STABLE', 'vagrantbox_url': ''},
         'ubuntu16': { 'installer': 'apt', 'vagrantbox': 'b2cloud/ubuntu16', 'vagrantbox_url': 'b2cloud-ubuntu16.box'},
}
