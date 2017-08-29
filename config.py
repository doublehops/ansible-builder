operating_system = 'debian'
webserver = 'nginx'
domain = 'autoauto.dev'

config = {
    'vagrantHostname': domain,
    'vagrantIPAddress': '192.168.30.101',
    'operating_system': operating_system,
    'outputPath': '/var/www/autoauto',
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
