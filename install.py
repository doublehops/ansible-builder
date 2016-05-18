#!/usr/bin/env python3

import sys, getopt, pprint
from collections import OrderedDict

from vagrant import *
from hardcodedvalues import *
from config import *
from tasks import *
from setupProvisioner import *
from printMessages import *


def main():

    outputPath = config['outputPath']
    setupProvisioner(outputPath, config['vagrantHostname'])
    createVagrantFile(config, oses)
    createTasks(config['tasks'], outputPath)
    cleanupProvisioner(outputPath)

    printPostInstall(config['vagrantIPAddress'], config['vagrantHostname'], config['outputPath'])


##########  END ##########

if __name__ == "__main__":
    main()
