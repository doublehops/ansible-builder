
###########  Define hard coded variables  ###########

oses = { 'debian': { 'installer': 'apt', 'vagrantbox': 'debian/jessie64' },
         'ubuntu': { 'installer': 'apt', 'vagrantbox': 'ubuntu/trusty64'},
         'redhat': { 'installer': 'yum', 'vagrantbox': ''},
         'centos': { 'installer': 'yum', 'vagrantbox': 'centos/7'},
         'freebsd': { 'installer': 'yum', 'vagrantbox': 'freebsd/FreeBSD-10.2-STABLE'},
}
