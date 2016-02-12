config = {
    'vagrantHostname': 're.sub.com',
    'vagrantIPAddress': '192.168.30.32',
    'operatingSystem': 'debian',
    'webServer': 'apache',
    'outputPath': 'output',
    'tasks': {
        'php7': {},
        'mysql': {
            'rootPassword': 'root12',
            'username': 'dev',
            'password': 'pass12',
            'database': 'proj',
        },
    },
}
