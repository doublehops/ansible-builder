import shutil

from functions import *

def include_php7(outputPath, params):

    if params['webserver'] is 'apache':
        phpHttpModule = 'libapache2-mod-php7.0'
    if params['webserver'] is 'nginx':
        phpHttpModule = 'php7.0-fpm'

    print('including php module')
    print('webserver: ', params['webserver'])
    shutil.copytree('provisioners/roles/php7', outputPath +'/provisioners/roles/php7')

    if params['webserver'] is 'apache':
        taskSrc = 'provisioners/roles/php7/tasks/php7-apache.yml'
    if params['webserver'] is 'nginx':
        taskSrc = '/provisioners/roles/php7/tasks/php7-nginx.yml'

    taskDest = outputPath +'/provisioners/roles/php7/tasks/main.yml'

    copyTemplate(taskSrc, taskDest)

    addRoleToPlaybook(outputPath, 'php7')
