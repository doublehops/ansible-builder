#!/usr/bin/env python3

import sys, getopt, pprint
from collections import OrderedDict

from modules.vagrant import *
from hardcodedvalues import *
from config import *
from tasks import *
from setupProvisioner import *
from printMessages import *


def main():

    if config['operating_system'] not in oses:
        print("operating_system is not valid: ", config['operating_system'])
        sys.exit(1)

    outputPath = config['outputPath']
    setupProvisioner(outputPath, config['vagrantHostname'], config['operating_system'])
    createVagrantFile(config, oses)
    createTasks(config['tasks'], outputPath)
    cleanupProvisioner(outputPath)

    #ubuntu16 vagrant box is not built from a base box so requires manual copy of private key
    #todo - build (or find) base box that has python 2.7 installed
    if config['operating_system'] is 'ubuntu16':
        copyTemplate('files/private_key', outputPath +'/private_key')

    printPostInstall(config['vagrantIPAddress'], config['vagrantHostname'], config['outputPath'])


##########  END ##########

if __name__ == "__main__":
    main()
