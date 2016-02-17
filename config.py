config = {
    'vagrantHostname': 'auto.api',
    'vagrantIPAddress': '192.168.30.39',
    'operatingSystem': 'ubuntu',
    'outputPath': '/var/www/autoproject',
    'tasks': {
        'apache': {
            'hostname': 'www.somedomain.com',
            'docroot': '/var/www',
        },
#        'php7': None,
#        'mysql': {
#            'rootPassword': 'root12',
#            'username': 'dev',
#            'password': 'pass12',
#            'database': 'proj',
#        },
    },
}
