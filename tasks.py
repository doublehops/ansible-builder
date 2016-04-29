import pprint 
import collections

from functions import *
from modules.webserver import *
from modules.php7 import *
from modules.add_ppas import *

def createTasks(tasks, outputPath):

    # Process tasks in a specific order
    eval('include_add_ppas')(outputPath, tasks['add_ppas'])
    tasks.pop('add_ppas')
    eval('include_webserver')(outputPath, tasks['webserver'])
    tasks.pop('webserver')
    eval('include_php7')(outputPath, tasks['php7'])
    tasks.pop('php7')

    # Process any remaining tasks where order not important
    for (key, value) in tasks.items():
        eval('include_'+ key)(outputPath, value)
        if value is None:
            print(key +' not null')

