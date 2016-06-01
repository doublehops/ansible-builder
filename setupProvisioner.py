import shutil, pprint, os, sys

from functions import *

def setupProvisioner(outputPath, vagrantHostname):

    print('-- Setting up provisioner --')

    if os.path.isdir(outputPath +'/Vagrantfile'):
        shutil.rmtree(outputPath +'/VagrantFile')
    if os.path.isdir(outputPath +'/provisioners'):
        shutil.rmtree(outputPath +'/provisioners')

    copyTemplate('provisioners_core/playbook.yml', outputPath +'/provisioners/playbook.yml')
    devHostFile = outputPath +'/provisioners/ansible_hosts'
    copyTemplate('provisioners_core/ansible_hosts', devHostFile, {'vagrantHostname': vagrantHostname})

    shutil.copytree('provisioners_core/roles/common', outputPath +'/provisioners/roles/common')

def cleanupProvisioner(outputPath):

    playbookFile = outputPath +'/provisioners/playbook.yml'
    copyTemplate(playbookFile, playbookFile, {'roles': ''})
