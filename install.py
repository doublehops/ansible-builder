#!/usr/bin/env python3

import sys, getopt

from vagrant import *

###########  Define options  ###########

def main():

    os = None # operating system
    devIPAddress = None
    outputPath = None
    webServer = None
    database = None
    hostname = None
    
    ###########  Define hard coded variables  ###########
    
    oses = { 'debian': { 'installer': 'apt', 'vagrantbox': 'debian/jessie64' },
             'ubuntu': { 'installer': 'apt', 'vagrantbox': 'ubuntu/trusty64'},
             'redhat': { 'installer': 'yum', 'vagrantbox': ''},
             'centos': { 'installer': 'yum', 'vagrantbox': 'centos/7'},
             'freebsd': { 'installer': 'yum', 'vagrantbox': 'freebsd/FreeBSD-10.2-STABLE'},
           }
    

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:o:i:d:', ["os=","output-path=","hostname=","ip="])
    except getopt.GetoptError:
        print("Bad parameters given")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-s' or opt == '--os':
            os = arg
        if opt == '-d' or opt == '--hostname':
            hostname = arg
        if opt == '-i' or opt == '--ip':
            devIPAddress = arg
        if opt == '-o' or opt == '--output-path':
            outputPath = arg
        if opt == '-w' or opt == '--web-server':
            webserver = arg

    print("os: ", os)
    print("vagrantbox: ", oses[os]['vagrantbox'])
    print("output-path: ", outputPath)
    print(oses[os]['installer'])

##########  START APPLICATION  ##########

    makeVagrantFile(hostname, devIPAddress, oses[os], outputPath)


##########  END ##########

if __name__ == "__main__":
    main()
