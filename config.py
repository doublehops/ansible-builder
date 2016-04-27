operatingSystem = 'ubuntu'
webserver = 'apache'

config = {
    'vagrantHostname': 'auto.api',
    'vagrantIPAddress': '192.168.30.39',
    'operatingSystem': operatingSystem,
    'outputPath': '/var/www/autoproject',
    'tasks': {
        'add_ppas': {
            'operatingSystem': operatingSystem,
        },
        'apache': {
            'hostname': 'auto.api',
            'docroot': '/var/www/web',
        },
        'php7': {
            'webserver': webserver,
        },
#        'mysql': {
#            'rootPassword': 'root12',
#            'username': 'dev',
#            'password': 'pass12',
#            'database': 'proj',
#        },
    },
}
