operating_system = 'debian'
webserver = 'nginx'

config = {
    'vagrantHostname': 'mac.api',
    'vagrantIPAddress': '192.168.30.98',
    'operating_system': operating_system,
    'outputPath': '/Users/b2cloud/projects/autoproject',
    'webserverProcessOwner': 'www-data', # nginx for centos6 nginx, www-data for all others
    'tasks': {
        'add_ppas': {
            'operating_system': operating_system,
        },
        'webserver': {
            'type': webserver,
            'hostname': 'mac.api',
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
