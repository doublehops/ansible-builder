import shutil

from functions import *

def include_add_ppas(outputPath, params):

    createPath(outputPath +'/provisioners/roles/add_ppas/tasks')

    copyTemplate('provisioners_core/roles/add_ppas/tasks/'+ params['operating_system'] +'.yml', outputPath + '/provisioners/roles/add_ppas/tasks/main.yml')

    addRoleToPlaybook(outputPath, 'add_ppas')
