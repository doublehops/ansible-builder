import shutil

from functions import *

def include_webserver(outputPath, params):

    family = getFamily(params['operating_system'])
    if family == 'debian':
        log_file_type = 'apache2'
    if family == 'redhat':
        log_file_type = 'httpd'

    templateFile = 'provisioners_core/roles/webserver/templates/local_dev_'+ params['type'] +'-'+ params['operating_system'] +'.j2'
    templateDest = outputPath +'/provisioners/roles/webserver/templates/default.conf'
    copyTemplate(templateFile, templateDest)

    copyTemplate('provisioners_core/roles/webserver/templates/index.j2', outputPath +'/provisioners/roles/webserver/templates/index.j2')

    templateVars = {'hostname': params['hostname'],
                    'docroot': params['docroot'],
                    'type': params['type'],
                    'log_file_type': log_file_type,
    }

    varsFile = 'provisioners_core/roles/webserver/vars/local_dev.yml'
    varsDest = outputPath +'/provisioners/roles/webserver/vars/local_dev.yml'
    copyTemplate(varsFile, varsDest, templateVars)

    vhostSrc = 'provisioners_templates/roles/webserver/tasks/'+params['operating_system'] +'-'+ params['type'] +'.yml'
    vhostDest = outputPath +'/provisioners/roles/webserver/tasks/main.yml'
    copyTemplate(vhostSrc, vhostDest, templateVars)

    handlersSrc = 'provisioners_templates/roles/webserver/handlers/main.yml'
    handlersDest = outputPath +'/provisioners/roles/webserver/handlers/main.yml'
    copyTemplate(handlersSrc, handlersDest)

    addRoleToPlaybook(outputPath, 'webserver')

