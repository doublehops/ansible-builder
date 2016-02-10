#!/usr/bin/env python3

import subprocess

from functions import *

def makeVagrantFile(hostname, ipAddress, os, outputPath):
    print('hostname: ', hostname)
    vagrantbox = os['vagrantbox']
    params = { 'hostname': hostname, 'ipaddress': ipAddress, 'vagrantbox': os['vagrantbox'] }
    source = 'files/Vagrantfile'
    dest = outputPath +"/Vagrantfile"
    copyTemplate(source, dest, params)
    #subprocess.call(['sed -e "s/__HOSTNAME__/'+ hostname +'/g" <'+ vagrantfile +' > '+ outputPath +'/Vagrantfile'], shell=True);

