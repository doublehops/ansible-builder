#!/usr/bin/env python3

import sys, getopt

from vagrant import *
from hardcodedvalues import *
from config import *


def main():

    makeVagrantFile(config, oses[config['operatingSystem']]['vagrantbox'])


##########  END ##########

if __name__ == "__main__":
    main()
