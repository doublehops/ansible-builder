import shutil

from functions import *

def include_php7(outputPath, params):

    #shutil.copytree('provisioners_core/roles/php7', outputPath +'/provisioners/roles/php7')

    taskSrc = 'provisioners_templates/roles/php7/tasks/php7-'+ params['webserver'] +'-'+ params['operating_system'] +'.yml'
    taskDest = outputPath +'/provisioners/roles/php7/tasks/main.yml'
    copyTemplate(taskSrc, taskDest)

    addRoleToPlaybook(outputPath, 'php7')
