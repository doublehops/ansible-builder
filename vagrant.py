#!/usr/bin/env python3

import subprocess

def stuff(hostname, ipAddress, os, outputPath):
    print('hostname: ', hostname)
    vagrantbox = os['vagrantbox']
    vagrantfile = 'files/Vagrantfile'
    subprocess.call(['sed -e "s/__HOSTNAME__/'+ hostname +'/g" <'+ vagrantfile +' > '+ outputPath +'/Vagrantfile'], shell=True);

