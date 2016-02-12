#!/usr/bin/env python3

import subprocess

from functions import *

def makeVagrantFile(config, vagrantbox):
    params = { 'hostname': config['vagrantHostname'],
               'ipaddress': config['vagrantIPAddress'],
               'vagrantbox': vagrantbox,
    }

    source = 'files/Vagrantfile'
    dest = config['outputPath'] +"/Vagrantfile"
    copyTemplate(source, dest, params)
    #subprocess.call(['sed -e "s/__HOSTNAME__/'+ hostname +'/g" <'+ vagrantfile +' > '+ outputPath +'/Vagrantfile'], shell=True);

