
from functions import *

def makeVagrantFile(config, vagrantbox):

    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': vagrantbox,
    }

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/Vagrantfile"
 
    copyTemplate(source, dest, params)
