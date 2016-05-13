import shutil

from functions import *

def include_add_ppas(outputPath, params):

    createPath(outputPath +'/provisioners/roles/add_ppas/tasks')

    if params['operating_system'] is 'ubuntu':
        copyTemplate('provisioners/roles/add_ppas/templates/ubuntu.yml', outputPath + '/provisioners/roles/add_ppas/tasks/main.yml')
    if params['operating_system'] is 'debian':
        copyTemplate('provisioners/roles/add_ppas/templates/debian.yml', outputPath + '/provisioners/roles/add_ppas/tasks/main.yml')

    addRoleToPlaybook(outputPath, 'add_ppas')
