operating_system = 'ubuntu16'
webserver = 'nginx'
domain = 'ansible.dev'

config = {
    'vagrantHostname': domain,
    'vagrantIPAddress': '192.168.30.76',
    'operating_system': operating_system,
    'outputPath': '/var/www/ansible-dev', # Filesystem path to where to create the Ansible scripts
    'webserverProcessOwner': 'www-data', # nginx for centos6 nginx, www-data for all others
    'tasks': {
        'add_ppas': {
            'operating_system': operating_system,
        },
        'webserver': {
            'type': webserver,
            'hostname': domain,
            'docroot': '/var/www/web',
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
