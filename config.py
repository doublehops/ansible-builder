operating_system = 'centos'
webserver = 'apache'

config = {
    'vagrantHostname': 'auto.api',
    'vagrantIPAddress': '192.168.30.39',
    'operating_system': operating_system,
    'outputPath': '/var/www/autoproject',
    'tasks': {
        'add_ppas': {
            'operating_system': operating_system,
        },
        'webserver': {
            'type': webserver,
            'hostname': 'auto.api',
            'docroot': '/var/www/web',
            'operating_system': operating_system,
        },
        'php7': {
            'webserver': webserver,
        },
        'database': {
            'type': 'mariadb',
            'operating_system': operating_system,
            'root_password': 'root12',
            'username': 'dev',
            'password': 'pass12',
            'database': 'proj',
            'test_database': 'proj_test',
        },
    },
}
