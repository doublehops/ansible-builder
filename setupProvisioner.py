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
#    createPath(outputPath)
#    createPath(outputPath +'/provisioners')
#    createPath(outputPath +'/provisioners/roles')
#    if os.path.isdir(outputPath +'/dev'):
#        shutil.rmtree(outputPath +'/dev')
#    shutil.copytree('dev', outputPath +'/dev')
#
#    shutil.copytree('provisioners/roles/common', outputPath +'/provisioners/roles/common')
#    shutil.copy('provisioners/playbook.yml', outputPath +'/provisioners')
#    devHostFile = outputPath +'/provisioners/ansible_hosts'
#    copyTemplate('provisioners/ansible_hosts', devHostFile, {'vagrantHostname': vagrantHostname})

def cleanupProvisioner(outputPath):

    playbookFile = outputPath +'/provisioners/playbook.yml'
    copyTemplate(playbookFile, playbookFile, {'roles': ''})
