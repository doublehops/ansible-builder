import shutil

from functions import *

def include_webserver(outputPath, params):

    shutil.copytree('provisioners/roles/webserver', outputPath +'/provisioners/roles/webserver')
    templateVars = {'hostname': params['hostname'],
                    'docroot': params['docroot'],
    }
    varsFile = outputPath +'/provisioners/roles/webserver/vars/local_dev.yml'
    copyTemplate(varsFile, varsFile, templateVars)

    vhostSrc = outputPath +'/provisioners/roles/webserver/tasks/'+ params['type'] +'.yml'
    vhostDest = outputPath +'/provisioners/roles/webserver/tasks/main.yml'
    copyTemplate(vhostSrc, vhostDest, templateVars)

    addRoleToPlaybook(outputPath, 'webserver')
