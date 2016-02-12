#!/usr/bin/env python3

import sys, getopt

from vagrant import *
from help import *
from config import *


def main():
    
    ###########  Define hard coded variables  ###########
    
    oses = { 'debian': { 'installer': 'apt', 'vagrantbox': 'debian/jessie64' },
             'ubuntu': { 'installer': 'apt', 'vagrantbox': 'ubuntu/trusty64'},
             'redhat': { 'installer': 'yum', 'vagrantbox': ''},
             'centos': { 'installer': 'yum', 'vagrantbox': 'centos/7'},
             'freebsd': { 'installer': 'yum', 'vagrantbox': 'freebsd/FreeBSD-10.2-STABLE'},
           }
    
    print("os: ", config['operatingSystem'])
    print("vagrantbox: ", oses[config['operatingSystem']]['vagrantbox'])
    print("output-path: ", config['outputPath'])
    print(oses[config['operatingSystem']]['installer'])

##########  START APPLICATION  ##########

    makeVagrantFile(config, oses[config['operatingSystem']]['vagrantbox'])


##########  END ##########

if __name__ == "__main__":
    main()
