operatingSystem = 'ubuntu'
webserver = 'nginx'

config = {
    'vagrantHostname': 'auto.api',
    'vagrantIPAddress': '192.168.30.39',
    'operatingSystem': operatingSystem,
    'outputPath': '/var/www/autoproject',
    'tasks': {
        'add_ppas': {
            'operatingSystem': operatingSystem,
        },
        'webserver': {
            'type': webserver,
            'hostname': 'auto.api',
            'docroot': '/var/www/web',
        },
        'php7': {
            'webserver': webserver,
        },
        'database': {
            'type': 'mysql',
            'operatingSystem': operatingSystem,
            'root_password': 'root12',
            'username': 'dev',
            'password': 'pass12',
            'database': 'proj',
            'test_database': 'proj_test',
        },
    },
}
