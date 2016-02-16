#!/usr/bin/env python3

import sys, getopt, pprint

from vagrant import *
from hardcodedvalues import *
from config import *
from tasks import *
from setupProvisioner import *


def main():

    outputPath = config['outputPath']
    setupProvisioner(outputPath)
    createVagrantFile(config, oses[config['operatingSystem']]['vagrantbox'])
    createTasks(config['tasks'], outputPath)
    cleanupProvisioner(outputPath)


##########  END ##########

if __name__ == "__main__":
    main()
