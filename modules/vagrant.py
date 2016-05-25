
from functions import *

def createVagrantFile(config, oses):

    print('-- Creating Vagrantfile --')

    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': oses[config['operating_system']]['vagrantbox'],
               'vagrantboxUrl': oses[config['operating_system']]['vagrantbox_url'],
               'webserverProcessOwner': config['webserverProcessOwner'],
    }

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/Vagrantfile"
 
    copyTemplate(source, dest, params)