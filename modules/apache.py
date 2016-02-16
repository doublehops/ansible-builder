import shutil

from functions import *

def include_apache(outputPath, params):
    print('including apache')
    shutil.copytree('provisioners/roles/apache', outputPath +'/provisioners/roles/apache')
    templateVars = {'hostname': params['hostname'],
                    'docroot': params['docroot'],
    }
    varsFile = outputPath +'/provisioners/roles/apache/vars/local_dev.yml'
    copyTemplate(varsFile, varsFile, templateVars)

    addRoleToPlaybook(outputPath, 'apache')
