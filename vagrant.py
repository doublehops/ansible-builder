
from functions import *

def createVagrantFile(config, vagrantbox):

    print('-- Creating Vagrantfile --')

    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': vagrantbox,
    }

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/Vagrantfile"
 
    copyTemplate(source, dest, params)
