import shutil, pprint, os

from functions import *

def setupProvisioner(outputPath):

    if os.path.isdir(outputPath +'/Vagrantfile'):
        shutil.rmtree(outputPath +'/VagrantFile')
    if os.path.isdir(outputPath +'/provisioners'):
        shutil.rmtree(outputPath +'/provisioners')
    createPath(outputPath)
    createPath(outputPath +'/provisioners')
    createPath(outputPath +'/provisioners/roles')

    shutil.copytree('provisioners/tasks', outputPath +'/provisioners/tasks')
    shutil.copy('provisioners/playbook.yml', outputPath +'/provisioners')

def cleanupProvisioner(outputPath):

    playbookFile = outputPath +'/provisioners/playbook.yml'
    copyTemplate(playbookFile, playbookFile, {'roles': ''})
