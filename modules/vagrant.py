
from functions import *

def createVagrantFile(config, oses):

    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': oses[config['operating_system']]['vagrantbox'],
               'vagrantboxUrl': oses[config['operating_system']]['vagrantbox_url'],
               'webserverProcessOwner': config['webserverProcessOwner'],
    }

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/tmp/Vagrantfile"
 
    copyTemplate(source, dest, params)
