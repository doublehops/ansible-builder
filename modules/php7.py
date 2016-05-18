import shutil

from functions import *

def include_php7(outputPath, params):

    taskSrc = 'provisioners/roles/php7/tasks/php7-'+ params['webserver'] +'-'+ params['operating_system'] +'.yml'

    print('including php module')
    print('webserver: ', params['webserver'])
    shutil.copytree('provisioners/roles/php7', outputPath +'/provisioners/roles/php7')

    print('webserver: '+ params['webserver']);
    print('taskSrc: '+ taskSrc)
    taskDest = outputPath +'/provisioners/roles/php7/tasks/main.yml'

    copyTemplate(taskSrc, taskDest)

    addRoleToPlaybook(outputPath, 'php7')
