#!/usr/bin/env python3

import sys, getopt, pprint

from vagrant import *
from hardcodedvalues import *
from config import *


def main():

    createVagrantFile(config, oses[config['operatingSystem']]['vagrantbox'])


##########  END ##########

if __name__ == "__main__":
    main()
