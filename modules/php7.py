import shutil

from functions import *

def include_php7(outputPath, params):

    if params['webserver'] == 'apache':
        phpHttpModule = 'libapache2-mod-php7.0'
        taskSrc = 'provisioners/roles/php7/tasks/php7-apache.yml'
    if params['webserver'] == 'nginx':
        phpHttpModule = 'php7.0-fpm'
        taskSrc = '/provisioners/roles/php7/tasks/php7-nginx.yml'

    print('including php module')
    print('webserver: ', params['webserver'])
    shutil.copytree('provisioners/roles/php7', outputPath +'/provisioners/roles/php7')

#    dv(params)
#    if params['webserver'] == 'apache':
#        taskSrc = 'provisioners/roles/php7/tasks/php7-apache.yml'
#    elif params['webserver'] == 'nginx':
#        taskSrc = '/provisioners/roles/php7/tasks/php7-nginx.yml'
#    else:
#        taskSrc = 'no source'

    print('webserver: '+ params['webserver']);
    print('taskSrc: '+ taskSrc)
    taskDest = outputPath +'/provisioners/roles/php7/tasks/main.yml'

    copyTemplate(taskSrc, taskDest)

    addRoleToPlaybook(outputPath, 'php7')
