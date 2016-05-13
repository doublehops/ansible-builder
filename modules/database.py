import shutil

from functions import *

def include_database(outputPath, params):

    shutil.copytree('provisioners/roles/database', outputPath +'/provisioners/roles/database')
    taskSrc = 'provisioners/roles/database/tasks/'+ params['type'] +'-'+ params['operating_system'] +'.yml'
    taskDest = outputPath +'/provisioners/roles/database/tasks/main.yml'
    copyTemplate(taskSrc, taskDest, params);
    
    varsFile = outputPath +'/provisioners/roles/database/vars/local_dev.yml'
    copyTemplate(varsFile, varsFile, params);

    addRoleToPlaybook(outputPath, 'database');

