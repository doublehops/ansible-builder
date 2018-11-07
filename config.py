operating_system = 'ubuntu'
webserver = 'apache2'
domain = 'ibaapp-api-vm'

config = {
    'vagrantHostname': domain,
    'vagrantIPAddress': '192.168.30.53',
    'operating_system': operating_system,
    'outputPath': '/Users/damien/projects/ibaapp-api-vm', # Filesystem path to where to create the Ansible scripts
    'webserverProcessOwner': 'www-data', # nginx for centos6 nginx, www-data for all others
    'tasks': {
        'webserver': {
            'type': webserver,
            'hostname': domain,
            'docroot': '/var/www',
            'operating_system': operating_system,
        },
        'php7': {
            'webserver': webserver,
            'operating_system': operating_system,
        },
        'database': {
            'type': 'mysql',
            'operating_system': operating_system,
            'root_password': 'root12',
            'username': 'dev',
            'password': 'pass12',
            'database': 'proj',
            'test_database': 'proj_test',
        },
    },
}
