import shutil

from functions import *

def include_webserver(outputPath, params):

    family = getFamily(params['operating_system'])
    if family == 'debian':
        log_file_type = 'apache2'
    if family == 'redhat':
        log_file_type = 'httpd'

    shutil.copytree('provisioners_core/roles/webserver', outputPath +'/provisioners/roles/webserver')
    templateVars = {'hostname': params['hostname'],
                    'docroot': params['docroot'],
                    'type': params['type'],
                    'log_file_type': log_file_type,
    }
    templateVars['hostTemplate'] = 'templates/local_dev_'+ params['type'] +'-'+ params['operating_system'] +'.j2'
    varsFile = outputPath +'/provisioners/roles/webserver/vars/local_dev.yml'
    copyTemplate(varsFile, varsFile, templateVars)

    vhostSrc = 'provisioners_templates/roles/webserver/tasks/'+params['operating_system'] +'-'+ params['type'] +'.yml'
    vhostDest = outputPath +'/provisioners/roles/webserver/tasks/main.yml'
    copyTemplate(vhostSrc, vhostDest, templateVars)

    addRoleToPlaybook(outputPath, 'webserver')
