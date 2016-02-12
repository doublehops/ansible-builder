config = {
    'vagrantHostname': 're.sub.com',
    'vagrantIPAddress': '192.168.30.32',
    'operatingSystem': 'debian',
    'outputPath': 'output',
    'tasks': {
        'apache': {},
        'php7': {},
        'mysql': {
            'rootPassword': 'root12',
            'username': 'dev',
            'password': 'pass12',
            'database': 'proj',
        },
    },
}
