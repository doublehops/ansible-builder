
from functions import *

def createVagrantFile(config, oses):

    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': oses[config['operating_system']]['vagrantbox'],
               'vagrantboxUrl': oses[config['operating_system']]['vagrantbox_url'],
               'webserverProcessOwner': config['webserverProcessOwner'],
               'auth': '',
    }

    if config['operating_system'] is 'ubuntu16':
        params['auth'] = """
    config.ssh.username = \"ubuntu\"
    config.ssh.private_key_path = \"private_key\""""

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/Vagrantfile"

    copyTemplate(source, dest, params)
